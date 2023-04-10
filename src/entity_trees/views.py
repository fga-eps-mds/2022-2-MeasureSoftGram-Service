"""
Módulo que agrupa as views relacionadas à árvore de entidades. Quando dizemos
árvore de entidades, estamos falando do relacionamentos entre as entidades.
Isso é:
* Características com subcaracterísticas
* Subcaracterísticas com medidas
"""
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from characteristics.models import SupportedCharacteristic
from entity_trees.serializers import (
    CharacteristicEntityRelationshipTreeSerializer,
    pre_config_to_entity_tree,
)
from organizations.models import Product
from pre_configs.models import PreConfig

from staticfiles import default_pre_config, sonarqube_supported_metrics


class SupportedEntitiesRelationshipTreeViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    ViewSet as entidades suportadas e suas relações no formato de árvore
    """
    serializer_class = CharacteristicEntityRelationshipTreeSerializer
    queryset = SupportedCharacteristic.objects.all()

    def list(self, request, *args, **kwargs):

        supported_measures = {}

        for item in sonarqube_supported_metrics.SONARQUBE_SUPPORTED_MEASURES:
            for k, v in item.items():
                supported_measures[k] = item[k]['metrics']

        tree = []
        id = 0

        for characteristic in default_pre_config.DEFAULT_PRE_CONFIG['characteristics']:
            subcharacteristics_list = []

            for subcharacteristic in characteristic['subcharacteristics']:
                measure_list = []

                for measure in subcharacteristic['measures']:
                    metrics_list = []

                    for metric in supported_measures[measure['key']]:
                        metrics_list.append({'id': id, 'name': metric, 'description': None, 'key': metric})
                        id += 1

                    measure_list.append({'id': id, 'name': measure['key'], 'description': None,
                                        'key': measure['key'], 'metrics': metrics_list})
                    id += 1

                subcharacteristics_list.append(
                    {'id': id, 'name': subcharacteristic['key'],
                        'description': None, 'key': subcharacteristic['key'],
                        'measures': measure_list})
                id += 1

            tree.append({'id': id, 'name': characteristic['key'], 'description': None,
                        'key': characteristic['key'], 'subcharacteristics': subcharacteristics_list})
            id += 1

        return Response(tree)


class PreConfigEntitiesRelationshipTreeViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Viewset que retorna as entidades de uma pré-configução e
    suas relações no formato de árvore
    """
    serializer_class = CharacteristicEntityRelationshipTreeSerializer
    queryset = SupportedCharacteristic.objects.all()

    def get_product(self):
        return get_object_or_404(
            Product,
            id=self.kwargs['product_pk'],
            organization_id=self.kwargs['organization_pk'],
        )

    def list(self, request, *args, **kwargs):
        product = self.get_product()
        current_pre_config = product.pre_configs.first()
        entity_tree = pre_config_to_entity_tree(current_pre_config)
        return Response(entity_tree)

# Generated by Django 4.0.6 on 2022-07-26 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_supportedmeasure_metrics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calculatedmeasure',
            options={'ordering': ['created_at']},
        ),
    ]

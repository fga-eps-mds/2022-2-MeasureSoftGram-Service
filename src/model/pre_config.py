import mongoengine as me


class PreConfig(me.Document):
    name = me.StringField(unique=True)
    characteristics = me.DictField()
    subcharacteristics = me.DictField()
    measures = me.ListField()

    def created_at(self):
        return self.id.generation_time

    def to_json(self):
        return {
            "_id": str(self.pk),
            "name": self.name,
            "characteristics": self.characteristics,
            "subcharacteristics": self.subcharacteristics,
            "measures": self.measures,
            "created_at": str(self.created_at()),
        }

    def to_lean_json(self):
        return{
            "_id": str(self.pk),
            "name": self.name,
            "created_at": str(self.created_at()),
        }

    def to_goal_json(self):
        return{
            "characteristics": self.characteristics,
            "subcharacteristics": self.subcharacteristics,
            "measures": self.measures,
            "characteristics_weights": self.characteristics_weights,
            "subcharacteristics_weights": self.subcharacteristics_weights,
            "measures_weights": self.measures_weights,
        }

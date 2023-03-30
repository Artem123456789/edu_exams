from collections import OrderedDict
from typing import Dict

from rest_framework import serializers
from rest_framework.serializers import ListSerializer


class BaseSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return super().to_representation(instance)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return super().create(validated_data)

    def _create_base_entity(self, validated_data: Dict, entity_class=None):
        if not entity_class:
            return None
        dict_data = {}
        fields = self.fields
        for k, value in validated_data.items():
            if isinstance(fields[k], BaseSerializer) or isinstance(
                fields[k], ListSerializer
            ):
                if (
                    isinstance(fields[k], ListSerializer)
                    and getattr(fields[k].child, "create", None)
                ) or (
                    isinstance(fields[k], BaseSerializer)
                    and getattr(fields[k], "create", None)
                ):
                    serialized_value = (
                        None if value is None else fields[k].create(value)
                    )
                    dict_data[k] = serialized_value
                else:
                    dict_data[k] = value
            else:
                dict_data[k] = value
        return entity_class(**dict_data)


class EntityUuidTypeIdOutputSerializer(BaseSerializer):
    uuid = serializers.UUIDField()


class EnumField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = OrderedDict(choices)
        super(EnumField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        for i in self._choices:
            if self._choices[i] == data:
                return self._choices[i]
        raise serializers.ValidationError(
            "Acceptable values are {0}.".format(list(self._choices.values()))
        )


class NoneSerializer(serializers.Serializer):
    pass

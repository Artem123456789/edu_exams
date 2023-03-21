from rest_framework import serializers
from libs.serialziers import BaseSerializer
from _auth.entities.auth_entities import RegisterInputEntity


class RegisterInputSerializer(BaseSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=30, required=True)

    def create(self, validated_data) -> RegisterInputEntity:
        return RegisterInputEntity(**validated_data)


class RegisterResponseSerializer(BaseSerializer):
    user_id = serializers.IntegerField(source="id")

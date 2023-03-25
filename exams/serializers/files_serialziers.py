from rest_framework import serializers

from exams.models import (
    OrdinaryQuestionFileModel,
    ComparisonQuestionFileModel,
)


class OrdinaryQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionFileModel
        fields = [
            "type",
            "file",
        ]


class ComparisonQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionFileModel
        fields = [
            "type",
            "file",
        ]

from rest_framework import serializers

from exams.models import (
    OrdinaryQuestionFile,
    ComparisonQuestionFile,
    OrdinaryQuestionAnswerFile,
    ComparisonQuestionOptionFile,
    ComparisonQuestionOptionAnswerFile,
)


class OrdinaryQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionFile
        fields = [
            "type",
            "file",
        ]


class ComparisonQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionFile
        fields = [
            "type",
            "file",
        ]


class OrdinaryQuestionAnswerFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionAnswerFile
        fields = [
            "type",
            "file",
        ]


class ComparisonQuestionOptionFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionOptionFile
        fields = [
            "type",
            "file",
        ]


class ComparisonQuestionOptionAnswerFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionOptionAnswerFile
        fields = [
            "type",
            "file",
        ]

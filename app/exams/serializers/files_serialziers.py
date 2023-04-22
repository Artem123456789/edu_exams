from rest_framework import serializers

from app.exams.models import (
    OrdinaryQuestionFile,
    ComparisonQuestionFile,
    OrdinaryQuestionAnswerFile,
    ComparisonQuestionOptionFile,
    ComparisonQuestionOptionAnswerFile,
    OriginalQuestionFile,
    OriginalBetweenQuestionFile,
    MultipleQuestion,
    MultipleQuestionAnswer,
)


class BaseFileMeta:
    fields = [
        "type",
        "file",
    ]


class OrdinaryQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = OrdinaryQuestionFile


class ComparisonQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = ComparisonQuestionFile


class OrdinaryQuestionAnswerFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = OrdinaryQuestionAnswerFile


class ComparisonQuestionOptionFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = ComparisonQuestionOptionFile


class ComparisonQuestionOptionAnswerFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = ComparisonQuestionOptionAnswerFile


class OriginalQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = OriginalQuestionFile


class OriginalBetweenQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = OriginalBetweenQuestionFile


class MultipleQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = MultipleQuestion


class MultipleQuestionAnswerFileModelSerializer(serializers.ModelSerializer):

    class Meta(BaseFileMeta):
        model = MultipleQuestionAnswer

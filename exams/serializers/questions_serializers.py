from rest_framework import serializers

from exams.models import (
    OrdinaryQuestionAnswer,
    OrdinaryQuestion,
    ComparisonQuestionOption,
    ComparisonQuestionOptionAnswer,
    ComparisonQuestion,
    OrdinaryQuestionFileModel,
    ComparisonQuestionFileModel,
)

from exams.serializers.files_serialziers import (
    OrdinaryQuestionFileModelSerializer,
    ComparisonQuestionFileModelSerializer,
)

"""
    Ordinary question answer
"""


class OrdinaryQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionAnswer
        fields = [
            "uuid",
            "text",
        ]


class OrdinaryQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()

    def get_answers(self, question: OrdinaryQuestion):
        question_answers = OrdinaryQuestionAnswer.objects.filter(question=question)
        return OrdinaryQuestionAnswerSerializer(question_answers, many=True).data

    def get_files(self, question: OrdinaryQuestion):
        files = OrdinaryQuestionFileModel.objects.filter(question=question)
        return OrdinaryQuestionFileModelSerializer(files, many=True).data

    class Meta:
        model = OrdinaryQuestion
        fields = [
            "uuid",
            "header",
            "description",
            "answers",
            "files",
        ]


"""
    Comparison question answer
"""


class ComparisonQuestionOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionOption
        fields = [
            "uuid",
            "text",
        ]


class ComparisonQuestionOptionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionOptionAnswer
        fields = [
            "uuid",
            "text",
        ]


class ComparisonQuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    option_answers = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()

    def get_options(self, question: ComparisonQuestion):
        options = ComparisonQuestionOption.objects.filter(question=question)
        return ComparisonQuestionOptionSerializer(options, many=True).data

    def get_option_answers(self, question: ComparisonQuestion):
        option_answers = ComparisonQuestionOptionAnswer.objects.filter(question=question)
        return ComparisonQuestionOptionAnswerSerializer(option_answers, many=True).data

    def get_files(self, question: ComparisonQuestion):
        files = ComparisonQuestionFileModel.objects.filter(question=question)
        return ComparisonQuestionFileModelSerializer(files, many=True).data

    class Meta:
        model = ComparisonQuestion
        fields = [
            "uuid",
            "header",
            "description",
            "options",
            "option_answers",
            "files",
        ]

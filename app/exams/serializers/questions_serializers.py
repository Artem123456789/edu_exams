from rest_framework import serializers

from app.exams.models import (
    OrdinaryQuestionAnswer,
    OrdinaryQuestion,
    ComparisonQuestionOption,
    ComparisonQuestionOptionAnswer,
    ComparisonQuestion,
    OrdinaryQuestionFile,
    ComparisonQuestionFile,
    OrdinaryQuestionAnswerFile,
    ComparisonQuestionOptionFile,
    ComparisonQuestionOptionAnswerFile,
)

from app.exams.serializers.files_serialziers import (
    OrdinaryQuestionFileModelSerializer,
    ComparisonQuestionFileModelSerializer,
    OrdinaryQuestionAnswerFileModelSerializer,
    ComparisonQuestionOptionFileModelSerializer,
    ComparisonQuestionOptionAnswerFileModelSerializer,
)

"""
    Ordinary question answer
"""


class OrdinaryQuestionAnswerSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    def get_files(self, answer: OrdinaryQuestionAnswer):
        files = OrdinaryQuestionAnswerFile.objects.filter(answer=answer)
        return OrdinaryQuestionAnswerFileModelSerializer(files, many=True).data

    class Meta:
        model = OrdinaryQuestionAnswer
        fields = [
            "uuid",
            "text",
            "files",
        ]


class OrdinaryQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()

    def get_answers(self, question: OrdinaryQuestion):
        question_answers = OrdinaryQuestionAnswer.objects.filter(question=question)
        return OrdinaryQuestionAnswerSerializer(question_answers, many=True).data

    def get_files(self, question: OrdinaryQuestion):
        files = OrdinaryQuestionFile.objects.filter(question=question)
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
    files = serializers.SerializerMethodField()

    def get_files(self, option: ComparisonQuestionOption):
        files = ComparisonQuestionOptionFile.objects.filter(option=option)
        return ComparisonQuestionOptionFileModelSerializer(files, many=True).data

    class Meta:
        model = ComparisonQuestionOption
        fields = [
            "uuid",
            "text",
            "files",
        ]


class ComparisonQuestionOptionAnswerSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    def get_files(self, option_answer: ComparisonQuestionOptionAnswer):
        files = ComparisonQuestionOptionAnswerFile.objects.filter(option_answer=option_answer)
        return ComparisonQuestionOptionAnswerFileModelSerializer(files, many=True).data

    class Meta:
        model = ComparisonQuestionOptionAnswer
        fields = [
            "uuid",
            "text",
            "files",
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
        files = ComparisonQuestionFile.objects.filter(question=question)
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

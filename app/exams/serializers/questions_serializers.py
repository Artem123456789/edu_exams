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
    OriginalQuestion,
    OriginalQuestionFile,
    OriginalBetweenQuestion,
    OriginalQuestionBetweenAnswerItem,
    OriginalBetweenQuestionFile,
)

from app.exams.serializers.files_serialziers import (
    OrdinaryQuestionFileModelSerializer,
    ComparisonQuestionFileModelSerializer,
    OrdinaryQuestionAnswerFileModelSerializer,
    ComparisonQuestionOptionFileModelSerializer,
    ComparisonQuestionOptionAnswerFileModelSerializer,
    OriginalQuestionFileModelSerializer,
    OriginalBetweenQuestionFileModelSerializer,
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
            "option",
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
        options = ComparisonQuestionOption.objects.filter(question=question).order_by("?")
        return ComparisonQuestionOptionSerializer(options, many=True).data

    def get_option_answers(self, question: ComparisonQuestion):
        option_answers = ComparisonQuestionOptionAnswer.objects.filter(question=question).order_by("?")
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
            "option",
        ]


"""
    Original question
"""


class OriginalQuestionSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    def get_files(self, question: OriginalQuestion):
        files = OriginalQuestionFile.objects.filter(question=question)
        return OriginalQuestionFileModelSerializer(files, many=True).data

    class Meta:
        model = OriginalQuestion
        fields = [
            "uuid",
            "header",
            "description",
            "files",
            "option",
        ]


"""
    Original between question
"""


class OriginalBetweenQuestionItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginalQuestionBetweenAnswerItem
        fields = [
            "uuid",
            "text",
            "order_index",
            "text_end",
        ]


class OriginalBetweenQuestionSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    def get_files(self, question: OriginalBetweenQuestion):
        files = OriginalBetweenQuestionFile.objects.filter(question=question)
        return OriginalBetweenQuestionFileModelSerializer(files, many=True).data

    def get_items(self, question: OriginalBetweenQuestion):
        items = OriginalQuestionBetweenAnswerItem.objects.filter(question=question).order_by("order_index")
        return OriginalBetweenQuestionItemSerializer(items, many=True).data

    class Meta:
        model = OriginalBetweenQuestion
        fields = [
            "uuid",
            "header",
            "description",
            "files",
            "items",
            "option",
        ]

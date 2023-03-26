from rest_framework import serializers, exceptions

from django.utils.translation import gettext as _

from exams.handlers.exams_handlers import (
    OrdinaryQuestionAnswersHandler,
    ComparisonQuestionAnswersHandler,
)
from exams.models import (
    OrdinaryQuestionUserAnswer,
    ComparisonQuestionUserAnswer,
)


class OrdinaryQuestionUserAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionUserAnswer
        fields = [
            "student_exam",
            "question",
            "answer",
        ]

    def validate(self, attrs):
        if OrdinaryQuestionAnswersHandler.is_answered(
            student_exam=attrs["student_exam"],
            question=attrs["question"],
        ):
            raise exceptions.PermissionDenied(_("Answer already sent"))

        return attrs


class ComparisonQuestionUserAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionUserAnswer
        fields = [
            "student_exam",
            "option",
            "option_answer",
        ]

    def validate(self, attrs):
        if ComparisonQuestionAnswersHandler.is_question_option_answered(
            student_exam=attrs["student_exam"],
            option=attrs["option"],
        ):
            raise exceptions.PermissionDenied(_("Answer already sent"))

        return attrs

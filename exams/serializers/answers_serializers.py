from rest_framework import serializers, exceptions
from datetime import datetime

from django.utils.translation import gettext as _

from exams.handlers.exams_handlers import (
    OrdinaryQuestionAnswersHandler,
    ComparisonQuestionAnswersHandler,
)
from exams.models import (
    OrdinaryQuestionUserAnswer,
    ComparisonQuestionUserAnswer, StudentExam,
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
        student_exam: StudentExam = attrs["student_exam"]

        if student_exam.is_not_finished():

            if datetime.now() > student_exam.get_deadline_datetime():
                raise exceptions.PermissionDenied(_("Time is up"))

            if OrdinaryQuestionAnswersHandler.is_answered(
                student_exam=student_exam,
                question=attrs["question"],
            ):
                raise exceptions.PermissionDenied(_("Answer already sent"))
        else:
            raise exceptions.PermissionDenied(_("Exam is finished"))

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
        student_exam: StudentExam = attrs["student_exam"]

        if student_exam.is_not_finished():

            if datetime.now() > student_exam.get_deadline_datetime():
                raise exceptions.PermissionDenied(_("Time is up"))

            if ComparisonQuestionAnswersHandler.is_question_option_answered(
                student_exam=student_exam,
                option=attrs["option"],
            ):
                raise exceptions.PermissionDenied(_("Answer already sent"))
        else:
            raise exceptions.PermissionDenied(_("Exam is finished"))

        return attrs

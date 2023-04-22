import pytz
from django.conf import settings

from rest_framework import serializers, exceptions
from datetime import datetime

from django.utils.translation import gettext as _

from app.exams.handlers.exams_handlers import (
    OrdinaryQuestionAnswersHandler,
    ComparisonQuestionAnswersHandler,
    OriginalQuestionAnswersHandler,
    OriginalQuestionBetweenAnswersHandler,
)
from app.exams.models import (
    OrdinaryQuestionUserAnswer,
    ComparisonQuestionUserAnswer,
    StudentExam,
    OriginalQuestionUserAnswer,
    OriginalQuestionBetweenUserAnswer,
)

local_tz = pytz.timezone(settings.TIME_ZONE)


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

            if datetime.now().astimezone(tz=local_tz) > student_exam.get_deadline_datetime().astimezone(tz=local_tz):
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

            if datetime.now().astimezone(tz=local_tz) > student_exam.get_deadline_datetime().astimezone(tz=local_tz):
                raise exceptions.PermissionDenied(_("Time is up"))

            if ComparisonQuestionAnswersHandler.is_question_option_answered(
                student_exam=student_exam,
                option=attrs["option"],
            ):
                raise exceptions.PermissionDenied(_("Answer already sent"))
        else:
            raise exceptions.PermissionDenied(_("Exam is finished"))

        return attrs


class OriginalQuestionUserAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginalQuestionUserAnswer
        fields = [
            "student_exam",
            "question",
            "text",
        ]

    def validate(self, attrs):
        student_exam: StudentExam = attrs["student_exam"]

        if student_exam.is_not_finished():

            if datetime.now().astimezone(tz=local_tz) > student_exam.get_deadline_datetime().astimezone(tz=local_tz):
                raise exceptions.PermissionDenied(_("Time is up"))

            if OriginalQuestionAnswersHandler.is_answered(
                student_exam=student_exam,
                question=attrs["question"],
            ):
                raise exceptions.PermissionDenied(_("Answer already sent"))
        else:
            raise exceptions.PermissionDenied(_("Exam is finished"))

        return attrs


class OriginalQuestionBetweenUserAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginalQuestionBetweenUserAnswer
        fields = [
            "item",
            "student_exam",
            "text",
        ]

    def validate(self, attrs):
        student_exam: StudentExam = attrs["student_exam"]

        if student_exam.is_not_finished():

            if datetime.now().astimezone(tz=local_tz) > student_exam.get_deadline_datetime().astimezone(tz=local_tz):
                raise exceptions.PermissionDenied(_("Time is up"))

            if OriginalQuestionBetweenAnswersHandler.is_answered(
                student_exam=student_exam,
                item=attrs["item"],
            ):
                raise exceptions.PermissionDenied(_("Answer already sent"))
        else:
            raise exceptions.PermissionDenied(_("Exam is finished"))

        return attrs

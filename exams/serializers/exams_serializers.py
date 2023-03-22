from rest_framework import serializers

from exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
)
from libs.serialziers import BaseSerializer


class StudentExamCreateSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StudentExam
        fields = [
            "uuid",
            "user",
            "exam",
        ]


class OrdinaryQuestionUserAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionUserAnswer
        fields = [
            "student_exam",
            "question",
            "answer",
        ]

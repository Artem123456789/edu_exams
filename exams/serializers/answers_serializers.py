from rest_framework import serializers

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


class ComparisonQuestionUserAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComparisonQuestionUserAnswer
        fields = [
            "student_exam",
            "option",
            "option_answer",
        ]

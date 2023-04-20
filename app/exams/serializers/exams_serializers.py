from rest_framework import serializers

from app.exams.models import (
    StudentExam,
    Exam,
    OrdinaryQuestion,
    ComparisonQuestion,
)
from app.exams.serializers.questions_serializers import (
    OrdinaryQuestionSerializer,
    ComparisonQuestionSerializer,
)
from app.libs.serialziers import BaseSerializer


class StudentExamCreateSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField()

    class Meta:
        model = StudentExam
        fields = [
            "uuid",
            "user_name",
            "exam",
        ]


class StudentExamResultsOutputSerializer(BaseSerializer):
    points = serializers.IntegerField()


class ExamRetrieveSerializer(serializers.ModelSerializer):
    ordinary_questions = serializers.SerializerMethodField()
    comparison_questions = serializers.SerializerMethodField()

    def get_ordinary_questions(self, exam: Exam):
        ordinary_questions = OrdinaryQuestion.objects.filter(exam=exam)
        return OrdinaryQuestionSerializer(ordinary_questions, many=True).data

    def get_comparison_questions(self, exam: Exam):
        comparison_questions = ComparisonQuestion.objects.filter(exam=exam)
        return ComparisonQuestionSerializer(comparison_questions, many=True).data

    class Meta:
        model = Exam
        fields = [
            "uuid",
            "name",
            "ordinary_questions",
            "comparison_questions",
            "hours_to_pass",
            "minutes_to_pass",
            "seconds_to_pass",
        ]

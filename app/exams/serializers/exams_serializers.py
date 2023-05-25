from rest_framework import serializers

from app.exams.models import (
    StudentExam,
    Exam,
    OrdinaryQuestion,
    ComparisonQuestion,
    OriginalQuestion,
    OriginalBetweenQuestion,
)
from app.exams.serializers.questions_serializers import (
    OrdinaryQuestionSerializer,
    ComparisonQuestionSerializer,
    OriginalQuestionSerializer,
    OriginalBetweenQuestionSerializer,
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
    max_points = serializers.IntegerField()
    hours_pass = serializers.IntegerField()
    minutes_pass = serializers.IntegerField()
    seconds_pass = serializers.IntegerField()


class ExamRetrieveSerializer(serializers.ModelSerializer):
    ordinary_questions = serializers.SerializerMethodField()
    comparison_questions = serializers.SerializerMethodField()
    original_questions = serializers.SerializerMethodField()
    original_between_questions = serializers.SerializerMethodField()

    def get_ordinary_questions(self, exam: Exam):
        ordinary_questions = OrdinaryQuestion.objects.filter(exam=exam)
        return OrdinaryQuestionSerializer(ordinary_questions, many=True).data

    def get_comparison_questions(self, exam: Exam):
        comparison_questions = ComparisonQuestion.objects.filter(exam=exam)
        return ComparisonQuestionSerializer(comparison_questions, many=True).data

    def get_original_questions(self, exam: Exam):
        original_questions = OriginalQuestion.objects.filter(exam=exam)
        return OriginalQuestionSerializer(original_questions, many=True).data

    def get_original_between_questions(self, exam: Exam):
        original_between_questions = OriginalBetweenQuestion.objects.filter(exam=exam)
        return OriginalBetweenQuestionSerializer(original_between_questions, many=True).data

    class Meta:
        model = Exam
        fields = [
            "uuid",
            "name",
            "ordinary_questions",
            "comparison_questions",
            "original_questions",
            "original_between_questions",
            "hours_to_pass",
            "minutes_to_pass",
            "seconds_to_pass",
        ]


class ExamListSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()

    def get_subject(self, exam: Exam):
        return exam.subject.name

    def get_school(self, exam: Exam):
        return exam.subject.school.name

    class Meta:
        model = Exam
        fields = [
            "uuid",
            "name",
            "subject",
            "school",
        ]

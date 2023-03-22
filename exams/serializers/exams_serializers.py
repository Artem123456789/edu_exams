from rest_framework import serializers

from exams.models import (
    StudentExam,
    Exam,
    OrdinaryQuestionUserAnswer,
    OrdinaryQuestion,
    OrdinaryQuestionAnswer,
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


class OrdinaryQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionAnswer
        fields = [
            "uuid",
            "text",
        ]


class OrdinaryQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    def get_answers(self, question: OrdinaryQuestion):
        question_answers = OrdinaryQuestionAnswer.objects.filter(question=question)
        return OrdinaryQuestionAnswerSerializer(question_answers, many=True).data

    class Meta:
        model = OrdinaryQuestion
        fields = [
            "uuid",
            "header",
            "description",
            "answers",
        ]


class ExamRetrieveSerializer(serializers.ModelSerializer):
    ordinary_questions = serializers.SerializerMethodField()

    def get_ordinary_questions(self, exam: Exam):
        exam_ordinary_questions = OrdinaryQuestion.objects.filter(exam=exam)
        return OrdinaryQuestionSerializer(exam_ordinary_questions, many=True).data

    class Meta:
        model = Exam
        fields = [
            "uuid",
            "name",
            "ordinary_questions",
        ]

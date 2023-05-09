from rest_framework import serializers

from app.exams.models import (
    StudentExam,
    Exam,
    OrdinaryQuestion,
    ComparisonQuestion,
    OriginalQuestion,
    OriginalBetweenQuestion,
    OrdinaryQuestionUserAnswer,
    OriginalQuestionUserAnswer,
    ComparisonQuestionUserAnswer,
    OriginalQuestionBetweenUserAnswer,
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


class OrdinaryQuestionUser(serializers.Serializer):
    question_header = serializers.CharField(source="question.header")
    question_description = serializers.CharField(source="question.description")

    right_answer = serializers.CharField(source="question.right_answer.text")
    right_answer_uuid = serializers.CharField(source="question.right_answer.uuid")

    user_answer = serializers.CharField(source="answer.text")
    user_answer_uuid = serializers.CharField(source="answer.uuid")


class OriginalQuestionUser(serializers.Serializer):
    question_header = serializers.CharField(source="question.header")
    question_description = serializers.CharField(source="question.description")
    right_answer = serializers.CharField(source="question.right_answer.text")
    user_answer = serializers.CharField(source="text")


class ComparisonQuestionUser(serializers.Serializer):
    question_uuid = serializers.CharField(source="option.question.uuid")
    question_header = serializers.CharField(source="option.question.header")
    question_description = serializers.CharField(source="option.question.description")

    right_answer = serializers.CharField(source="option.text")
    right_answer_uuid = serializers.CharField(source="option.uuid")

    user_answer = serializers.CharField(source="option_answer.text")
    user_answer_uuid = serializers.CharField(source="option_answer.uuid")


class OriginalBetweenQuestionUser(serializers.Serializer):
    question_uuid = serializers.CharField(source="item.question.uuid")
    question_header = serializers.CharField(source="item.question.header")
    question_description = serializers.CharField(source="item.question.description")

    item_text = serializers.CharField(source="item.text")
    item_text_answer = serializers.CharField(source="item.text_answer")
    order_index = serializers.CharField(source="item.order_index")

    user_answer_text = serializers.CharField(source="text")


class StudentExamRetrieveSerializer(serializers.ModelSerializer):
    ordinary_question_answers = serializers.SerializerMethodField()
    original_question_answers = serializers.SerializerMethodField()
    comparison_question_answers = serializers.SerializerMethodField()
    original_between_answers = serializers.SerializerMethodField()

    def get_ordinary_question_answers(self, student_exam: StudentExam):
        answers = OrdinaryQuestionUserAnswer.objects.filter(student_exam=student_exam)
        return OrdinaryQuestionUser(answers, many=True).data

    def get_original_question_answers(self, student_exam: StudentExam):
        answers = OriginalQuestionUserAnswer.objects.filter(student_exam=student_exam)
        return OriginalQuestionUser(answers, many=True).data

    def get_comparison_question_answers(self, student_exam: StudentExam):
        answers = ComparisonQuestionUserAnswer.objects.filter(student_exam=student_exam)
        return ComparisonQuestionUser(answers, many=True).data

    def get_original_between_answers(self, student_exam: StudentExam):
        answers = OriginalQuestionBetweenUserAnswer.objects.filter(student_exam=student_exam)
        return OriginalBetweenQuestionUser(answers, many=True).data

    class Meta:
        model = StudentExam
        fields = [
            "ordinary_question_answers",
            "original_question_answers",
            "comparison_question_answers",
            "original_between_answers",
        ]


class StudentExamResultsOutputSerializer(BaseSerializer):
    points = serializers.IntegerField()


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

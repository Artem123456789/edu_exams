from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
    Exam, ComparisonQuestionUserAnswer,
)
from rest_framework.viewsets import GenericViewSet

from exams.serializers.answers_serializers import (
    OrdinaryQuestionUserAnswerCreateSerializer,
    ComparisonQuestionUserAnswerCreateSerializer,
)
from exams.serializers.exams_serializers import (
    StudentExamCreateSerializer,
    ExamRetrieveSerializer,
)


class ExamViewSet(
    generics.RetrieveAPIView,
    GenericViewSet,
):
    queryset = Exam.objects.all()

    def get_serializer_class(self):
        return {
            "retrieve": ExamRetrieveSerializer,
        }[self.action]


class StudentExamsViewSet(
    generics.CreateAPIView,
    GenericViewSet,
):
    queryset = StudentExam.objects.all()

    def get_serializer_class(self):
        return {
            "create": StudentExamCreateSerializer,
        }[self.action]


class OrdinaryQuestionUserAnswerViewSet(
    generics.CreateAPIView,
    GenericViewSet,
):
    queryset = OrdinaryQuestionUserAnswer.objects.all()

    def get_serializer_class(self):
        return {
            "create": OrdinaryQuestionUserAnswerCreateSerializer,
        }[self.action]


class ComparisonQuestionUserAnswerViewSet(
    generics.CreateAPIView,
    GenericViewSet,
):
    queryset = ComparisonQuestionUserAnswer.objects.all()

    def get_serializer_class(self):
        return {
            "create": ComparisonQuestionUserAnswerCreateSerializer,
        }[self.action]

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
    Exam,
)
from rest_framework.viewsets import GenericViewSet

from exams.serializers.exams_serializers import (
    StudentExamCreateSerializer,
    OrdinaryQuestionUserAnswerCreateSerializer,
    ExamRetrieveSerializer,
)


class ExamViewSet(
    generics.RetrieveAPIView,
    GenericViewSet,
):
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return {
            "retrieve": ExamRetrieveSerializer,
        }[self.action]


class StudentExamsViewSet(
    generics.CreateAPIView,
    GenericViewSet,
):
    queryset = StudentExam.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return {
            "create": StudentExamCreateSerializer,
        }[self.action]


class OrdinaryQuestionUserAnswerViewSet(
    generics.CreateAPIView,
    GenericViewSet,
):
    queryset = OrdinaryQuestionUserAnswer.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return {
            "create": OrdinaryQuestionUserAnswerCreateSerializer,
        }[self.action]

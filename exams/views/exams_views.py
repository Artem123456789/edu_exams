from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
)
from rest_framework.viewsets import GenericViewSet

from exams.serializers.exams_serializers import (
    StudentExamCreateSerializer,
    OrdinaryQuestionUserAnswerCreateSerializer,
)


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

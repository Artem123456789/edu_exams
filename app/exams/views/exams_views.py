from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response

from app.exams.handlers.exams_handlers import (
    StudentExamsHandler,
)
from app.exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
    Exam,
    ComparisonQuestionUserAnswer,
    OriginalQuestionUserAnswer,
)
from rest_framework.viewsets import GenericViewSet

from app.exams.serializers.answers_serializers import (
    OrdinaryQuestionUserAnswerCreateSerializer,
    ComparisonQuestionUserAnswerCreateSerializer,
    OriginalQuestionUserAnswerCreateSerializer,
)
from app.exams.serializers.exams_serializers import (
    StudentExamCreateSerializer,
    ExamRetrieveSerializer,
    StudentExamResultsOutputSerializer,
    ExamListSerializer,
)


class ExamViewSet(
    generics.RetrieveAPIView,
    generics.ListAPIView,
    GenericViewSet,
):
    queryset = Exam.objects.all()

    def get_serializer_class(self):
        return {
            "list": ExamListSerializer,
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
            "get_student_exam_results": StudentExamResultsOutputSerializer,
        }[self.action]

    @action(methods=["get"], detail=True, url_path="results")
    def get_student_exam_results(self, request, *args, **kwargs):
        student_exam = self.get_object()
        entity = StudentExamsHandler().get_student_exam_results(student_exam=student_exam)

        return Response(self.get_serializer_class()(entity).data)

    @action(methods=["post"], detail=True)
    def finish(self, request, *args, **kwargs):
        student_exam = self.get_object()

        StudentExamsHandler.finish_student_exam(student_exam=student_exam)

        return Response()


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


class OriginalQuestionUserAnswerViewSet(
    generics.CreateAPIView,
    GenericViewSet,
):
    queryset = OriginalQuestionUserAnswer.objects.all()

    def get_serializer_class(self):
        return {
            "create": OriginalQuestionUserAnswerCreateSerializer,
        }[self.action]

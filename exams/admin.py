from django.contrib import admin
from .models import (
    School,
    Subject,
    Exam,
    OrdinaryQuestion,
    OrdinaryQuestionAnswer,
    StudentExam,
    OrdinaryQuestionUserAnswer,
    ComparisonQuestion,
    ComparisonQuestionOption,
    ComparisonQuestionOptionAnswer,
    ComparisonQuestionUserAnswer,
)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "school",
    )

    list_filter = (
        "school",
    )

    search_fields = (
        "name",
    )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
    )

    list_filter = (
        "subject",
    )

    search_fields = (
        "name",
    )


@admin.register(OrdinaryQuestion)
class OrdinaryQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )

    list_filter = (
        "exam",
    )

    search_fields = (
        "header",
    )


@admin.register(OrdinaryQuestionAnswer)
class OrdinaryQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
    )

    list_filter = (
        "is_correct",
    )

    search_fields = (
        "question",
    )


@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = (
        "user_name",
        "exam",
    )

    list_filter = (
        "user_name",
        "exam",
    )


@admin.register(OrdinaryQuestionUserAnswer)
class OrdinaryQuestionUserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "answer",
    )


@admin.register(ComparisonQuestion)
class ComparisonQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )

    list_filter = (
        "exam",
    )

    search_fields = (
        "header",
    )


@admin.register(ComparisonQuestionOption)
class ComparisonQuestionOptionAdmin(admin.ModelAdmin):
    list_display = (
        "text",
    )

    list_filter = (
        "text",
    )


@admin.register(ComparisonQuestionOptionAnswer)
class ComparisonQuestionOptionAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "text",
    )

    list_filter = (
        "text",
    )


@admin.register(ComparisonQuestionUserAnswer)
class ComparisonQuestionUserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "option",
        "option_answer",
    )

    list_filter = (
        "option",
        "option_answer",
    )

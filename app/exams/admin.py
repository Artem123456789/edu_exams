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
    OrdinaryQuestionFile,
    ComparisonQuestionFile,
    OrdinaryQuestionAnswerFile,
    ComparisonQuestionOptionFile,
    ComparisonQuestionOptionAnswerFile,
    OriginalQuestion,
    OriginalQuestionAnswer,
    OriginalQuestionUserAnswer,
    OriginalQuestionFile,
    OriginalBetweenQuestion,
    OriginalQuestionBetweenAnswerItem,
    OriginalQuestionBetweenUserAnswer,
    OriginalBetweenQuestionFile,
    MultipleQuestion,
    MultipleQuestionAnswer,
    MultipleQuestionUserAnswer,
    MultipleQuestionFile,
    MultipleQuestionAnswerFile,
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


@admin.register(OrdinaryQuestionFile)
class OrdinaryQuestionFileModelAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "file",
    )


@admin.register(ComparisonQuestionFile)
class ComparisonQuestionFileModelAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "file",
    )


@admin.register(OrdinaryQuestionAnswerFile)
class OrdinaryQuestionAnswerFileAdmin(admin.ModelAdmin):
    list_display = (
        "answer",
        "file",
    )


@admin.register(ComparisonQuestionOptionFile)
class ComparisonQuestionOptionFileAdmin(admin.ModelAdmin):
    list_display = (
        "option",
        "file",
    )


@admin.register(ComparisonQuestionOptionAnswerFile)
class ComparisonQuestionOptionAnswerFileAdmin(admin.ModelAdmin):
    list_display = (
        "option_answer",
        "file",
    )


@admin.register(OriginalQuestion)
class OriginalQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )

    list_filter = (
        "exam",
    )

    search_fields = (
        "header",
    )


@admin.register(OriginalQuestionAnswer)
class OriginalQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
    )

    search_fields = (
        "question",
    )


@admin.register(OriginalQuestionUserAnswer)
class OriginalQuestionUserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "text",
    )


@admin.register(OriginalQuestionFile)
class OriginalQuestionFileAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "file",
    )


@admin.register(OriginalBetweenQuestion)
class OriginalBetweenQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )

    list_filter = (
        "exam",
    )

    search_fields = (
        "header",
    )


@admin.register(OriginalQuestionBetweenAnswerItem)
class OriginalQuestionBetweenAnswerItemAdmin(admin.ModelAdmin):
    list_display = (
        "question",
    )

    search_fields = (
        "question",
    )


@admin.register(OriginalQuestionBetweenUserAnswer)
class OriginalQuestionBetweenUserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "text",
    )


@admin.register(OriginalBetweenQuestionFile)
class OriginalBetweenQuestionFileAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "file",
    )


@admin.register(MultipleQuestion)
class MultipleQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )

    list_filter = (
        "exam",
    )

    search_fields = (
        "header",
    )


@admin.register(MultipleQuestionAnswer)
class MultipleQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
    )

    list_filter = (
        "is_correct",
    )

    search_fields = (
        "question",
    )


@admin.register(MultipleQuestionUserAnswer)
class MultipleQuestionUserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "answer",
    )


@admin.register(MultipleQuestionFile)
class MultipleQuestionFileAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "file",
    )


@admin.register(MultipleQuestionAnswerFile)
class MultipleQuestionAnswerFileAdmin(admin.ModelAdmin):
    list_display = (
        "answer",
        "file",
    )

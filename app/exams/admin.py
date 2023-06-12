from io import BytesIO

import pandas as pd
from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from .admin_reports import exam_report
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
)

from transliterate.utils import _

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

    actions = (
        "report",
    )

    def _init_report(self, action, queryset, filename):
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine="xlsxwriter")
            df = action(queryset)
            df.to_excel(writer, "Page1")
            writer.save()
            xlsx_data = b.getvalue()
            response = HttpResponse(
                xlsx_data, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            response["Content-Disposition"] = f'attachment; filename="{timezone.now().date()}-{filename}"'
            return response

    @admin.action(description=_("Отчет о результатах тестирования"))
    def report(self, request, queryset):
        return self._init_report(action=exam_report, queryset=queryset, filename="report.xlsx")


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


@admin.register(OrdinaryQuestionFile)
class OrdinaryQuestionFileModelAdmin(admin.ModelAdmin):
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
class OrdinaryQuestionUserAnswerAdmin(admin.ModelAdmin):
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

import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext as _

from exams.contants import FileType
from exams.utils.file_upload import file_ordinary_question_upload
from libs.base_models import (
    NamedModel,
    QuestionModel,
)

User = get_user_model()


class School(NamedModel):
    """
        Образовательное учреждение
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        verbose_name = _("Образовательное учреждение")
        verbose_name_plural = _("Образовательные учреждения")

    def __str__(self):
        return self.name


class Subject(NamedModel):
    """
        Дисциплина
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Дисциплина")
        verbose_name_plural = _("Дисциплины")

    def __str__(self):
        return f"{self.name} {self.school.name}"


class Exam(NamedModel):
    """
        Экзамен
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Экзамен")
        verbose_name_plural = _("Экзамены")

    def __str__(self):
        return self.name


class OrdinaryQuestion(QuestionModel):
    """
        Вопрос с одним вариантом ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    right_answer_points = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Вопрос с одним вариантом ответа")
        verbose_name_plural = _("Вопросы с одним вариантом ответа")


class OrdinaryQuestionAnswer(models.Model):
    """
        Ответ на вопрос с одним вариантом ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.ForeignKey(OrdinaryQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    is_correct = models.BooleanField()

    class Meta:
        verbose_name = _("Ответ на вопрос с одним вариантом ответа")
        verbose_name_plural = _("Ответы на вопрос с одним вариантом ответа")

    def __str__(self):
        return self.text[:20]


class StudentExam(TimeStampedModel):
    """
        Экзамен студента
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user_name = models.CharField(max_length=100, default="")
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Экзамен студента")
        verbose_name_plural = _("Экзамены студента")

    def __str__(self):
        return f"{self.user_name} {self.exam}"


class OrdinaryQuestionUserAnswer(TimeStampedModel):
    """
        Ответ пользователя на вопрос с одним вариантом ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student_exam = models.ForeignKey(StudentExam, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(OrdinaryQuestion, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(OrdinaryQuestionAnswer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Ответ пользователя на вопрос с одним вариантом ответа")
        verbose_name_plural = _("Ответы пользователя на вопрос с одним вариантом ответа")

    def __str__(self):
        return f"{str(self.question)} {str(self.answer)}"


class ComparisonQuestion(QuestionModel):
    """
        Вопрос с сопоставлением ответов
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Вопрос с сопоставлением ответов")
        verbose_name_plural = _("Вопросы с сопоставлением ответов")


class ComparisonQuestionOptionAnswer(models.Model):
    """
        Ответ на опцию вопроса с сопоставлением
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.ForeignKey(ComparisonQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    class Meta:
        verbose_name = _("Ответ на опцию вопроса с сопоставлением")
        verbose_name_plural = _("Ответы на опцию вопроса с сопоставлением")

    def __str__(self):
        return self.text[:20]


class ComparisonQuestionOption(models.Model):
    """
        Опция вопроса с сопоставлением ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.ForeignKey(ComparisonQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    option_answer = models.OneToOneField(ComparisonQuestionOptionAnswer, on_delete=models.SET_NULL, null=True)

    right_answer_points = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Опция вопроса с сопоставлением ответа")
        verbose_name_plural = _("Опции вопроса с сопоставлением ответа")

    def __str__(self):
        return self.text[:20]


class ComparisonQuestionUserAnswer(TimeStampedModel):
    """
        Ответ пользователя на вопрос с сопоставлением ответов
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student_exam = models.ForeignKey(StudentExam, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(ComparisonQuestionOption, on_delete=models.SET_NULL, null=True)
    option_answer = models.ForeignKey(ComparisonQuestionOptionAnswer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Ответ пользователя на вопрос с сопоставлением ответов")
        verbose_name_plural = _("Ответы пользователя на вопрос с сопоставлением ответов")

    def __str__(self):
        return f"{str(self.option)} {str(self.option_answer)}"


class OrdinaryQuestionFileModel(models.Model):
    """
        Файлы обычных вопросов
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    question = models.ForeignKey(
        OrdinaryQuestion, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_ordinary_question_upload)

    class Meta:
        verbose_name = _("Файл обычного вороса")
        verbose_name_plural = _("Файлы обычных вопросов")

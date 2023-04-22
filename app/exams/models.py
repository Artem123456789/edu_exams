import uuid
from datetime import (
    timedelta,
    datetime,
)

from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext as _

from app.exams.contants import FileType
from app.exams.utils.file_upload import (
    file_ordinary_question_upload,
    file_comparison_question_upload,
    file_ordinary_answer_upload,
    file_comparison_option_upload,
    file_comparison_option_answer_upload,
    file_original_question_upload,
    file_original_between_question_upload,
)
from app.libs.base_models import (
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

    #  Ограничение по времени для сдачи экзамена
    hours_to_pass = models.SmallIntegerField(null=True)
    minutes_to_pass = models.SmallIntegerField(null=True)
    seconds_to_pass = models.SmallIntegerField(null=True)

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

    end_datetime = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _("Экзамен студента")
        verbose_name_plural = _("Экзамены студента")

    def get_deadline_datetime(self) -> datetime:
        return (self.created +
                timedelta(minutes=self.exam.minutes_to_pass)
                + timedelta(hours=self.exam.hours_to_pass)
                + timedelta(seconds=self.exam.seconds_to_pass)
                )

    def is_not_finished(self) -> bool:
        return self.end_datetime is None

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
        return f"{self.question} {self.answer}"


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
        return f"{self.option} {self.option_answer}"


class OriginalQuestion(QuestionModel):
    """
        Вопрос с ответом пользователя
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    right_answer_points = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Вопрос с ответом пользователя")
        verbose_name_plural = _("Вопроcы с ответами пользователей")


class OriginalQuestionAnswer(models.Model):
    """
        Ответ на вопрос с ответом пользователя
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.ForeignKey(OriginalQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    class Meta:
        verbose_name = _("Ответ на вопрос с ответом пользователя")
        verbose_name_plural = _("Ответы на вопрос с ответами пользователей")

    def __str__(self):
        return self.text[:20]


class OriginalQuestionUserAnswer(TimeStampedModel):
    """
        Ответ пользователя на вопрос c ответом пользователя
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student_exam = models.ForeignKey(StudentExam, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(OriginalQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    class Meta:
        verbose_name = _("Ответ пользователя на вопрос c ответом пользователя")
        verbose_name_plural = _("Ответы пользователей на вопросы c ответами пользователей")

    def __str__(self):
        return f"{self.question} {self.text[:20]}"


class OriginalBetweenQuestion(QuestionModel):
    """
        Вопрос с вписыванием между текстом
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Вопрос с вписыванием между текстом")
        verbose_name_plural = _("Вопросы со вписыванием между текстом")


class OriginalQuestionBetweenAnswerItem(models.Model):
    """
        Элемент вопроса со вписыванием между текстом
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.ForeignKey(OriginalBetweenQuestion, on_delete=models.SET_NULL, null=True)

    text = models.TextField()
    text_answer = models.TextField(null=True, blank=True)

    right_answer_points = models.SmallIntegerField(null=True)
    order_index = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Элемент вопроса со вписыванием между текстом")
        verbose_name_plural = _("Элементы вопросов со вписыванием между текстом")

    def __str__(self):
        return self.text[:20]


class OriginalQuestionBetweenUserAnswer(models.Model):
    """
        Ответ пользователя на элемент вопроса со вписыванием между текстом
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    item = models.ForeignKey(OriginalQuestionBetweenAnswerItem, on_delete=models.SET_NULL, null=True)
    student_exam = models.ForeignKey(StudentExam, on_delete=models.SET_NULL, null=True)

    text = models.TextField()

    class Meta:
        verbose_name = _("Ответ пользователя на элемент вопроса со вписыванием между текстом")
        verbose_name_plural = _("Ответы пользователей на элементы вопросов со вписыванием между текстом")

    def __str__(self):
        return self.text[:20]


# File models

class OrdinaryQuestionFile(models.Model):
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


class ComparisonQuestionFile(models.Model):
    """
        Файлы вопросов с сопоставлением
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    question = models.ForeignKey(
        ComparisonQuestion, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_comparison_question_upload)

    class Meta:
        verbose_name = _("Файл вопроса с сопоставлением")
        verbose_name_plural = _("Файлы вопросов с сопоставлением")


class OriginalQuestionFile(models.Model):
    """
        Файлы вопросов с ответами пользователей
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    question = models.ForeignKey(
        OriginalQuestion, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_ordinary_question_upload)

    class Meta:
        verbose_name = _("Файлы вопросов с ответами пользователей")
        verbose_name_plural = _("Файлы вопросов с ответами пользователей")


class OrdinaryQuestionAnswerFile(models.Model):
    """
        Файлы ответов на обычные вопросы
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    answer = models.ForeignKey(
        OrdinaryQuestionAnswer, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_ordinary_answer_upload)

    class Meta:
        verbose_name = _("Файл ответа на обычный вопрос")
        verbose_name_plural = _("Файлы ответов на обычные вопрос")


class ComparisonQuestionOptionFile(models.Model):
    """
        Файлы опций вопросов с сопоставлением
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    option = models.ForeignKey(
        ComparisonQuestionOption, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_comparison_option_upload)

    class Meta:
        verbose_name = _("Файл опции вопроса с сопоставлением")
        verbose_name_plural = _("Файлы опций вопросов с сопоставлением")


class ComparisonQuestionOptionAnswerFile(models.Model):
    """
        Файлы ответов на опции вопросов с сопоставлением
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    option_answer = models.ForeignKey(
        ComparisonQuestionOptionAnswer, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_comparison_option_answer_upload)

    class Meta:
        verbose_name = _("Файл ответа на опцию вопроса с сопоставлением")
        verbose_name_plural = _("Файлы ответов на опции вопросов с сопоставлением")


class OriginalBetweenQuestionFile(models.Model):
    """
        Файл вопроса с вписыванием между текстом
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), default=FileType.TYPE_IMAGE)
    question = models.ForeignKey(
        OriginalBetweenQuestion, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to=file_original_between_question_upload)

    class Meta:
        verbose_name = _("Файл вопроса с вписыванием между текстом")
        verbose_name_plural = _("Файлы вопросов с вписыванием между текстом")

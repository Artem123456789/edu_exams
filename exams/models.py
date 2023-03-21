import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel

from libs.base_models import (
    NamedModel,
    QuestionModel,
)

User = get_user_model()


class School(NamedModel):
    """
        Образовательное учреждение
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.name


class Subject(NamedModel):
    """
        Дисциплина
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.school.name}"


class Exam(NamedModel):
    """
        Экзамен
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.subject.name}"


class OrdinaryQuestion(QuestionModel):
    """
        Вопрос с одним вариантом ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)


class OrdinaryQuestionAnswer(models.Model):
    """
        Ответ на вопрос с одним вариантом ответа
    """
    question = models.ForeignKey(OrdinaryQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text[:20]


class StudentExam(TimeStampedModel):
    """
        Экзамен студента
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.name} {self.exam}"


class OrdinaryQuestionUserAnswer(TimeStampedModel):
    """
        Ответ пользователя на вопрос с одним вариантом ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    question = models.ForeignKey(OrdinaryQuestion, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(OrdinaryQuestionAnswer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{str(self.question)} {str(self.answer)}"


class ComparisonQuestion(QuestionModel):
    """
        Вопрос с сопоставлением ответов
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)


class ComparisonQuestionOption(models.Model):
    """
        Опция вопроса с сопоставлением ответа
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    question = models.ForeignKey(ComparisonQuestion, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


class ComparisonQuestionOptionAnswer(models.Model):
    """
        Ответ на опцию вопроса с сопоставлением
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    text = models.TextField()
    option = models.OneToOneField(ComparisonQuestionOption, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text[:20]


class ComparisonQuestionUserAnswer(TimeStampedModel):
    """
        Ответ пользователя на вопрос с сопоставлением ответов
    """
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    student_exam = models.ForeignKey(StudentExam, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(ComparisonQuestionOption, on_delete=models.SET_NULL, null=True)
    option_answer = models.ForeignKey(ComparisonQuestionOptionAnswer, on_delete=models.SET_NULL, null=True)

    def __str(self):
        return f"{str(self.option)} {str(self.option_answer)}"

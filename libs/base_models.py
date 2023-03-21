from django.db import models


class NamedModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=("Название"), blank=True, null=True)

    class Meta:
        abstract = True


class QuestionModel(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.header

    class Meta:
        abstract = True

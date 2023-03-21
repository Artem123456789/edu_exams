from django.db import models

from pharmacy.constants import MAX_LEN_CHAR_FIELD


class NamedModel(models.Model):
    name = models.CharField(max_length=MAX_LEN_CHAR_FIELD, verbose_name=("Название"), blank=True, null=True)

    class Meta:
        abstract = True

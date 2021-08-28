from django.db import models


class Specialization(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'

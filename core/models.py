from django.db import models


class Perks(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return f'<Специализация: {self.name}>'

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'


class Tag(models.Model):
    name = models.CharField('Название', max_length=255)
    perks = models.ManyToManyField('Perks', related_name='tags')

    def __str__(self):
        return f'<Тег: {self.name}>'

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

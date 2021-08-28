from django.db import models


class Perks(models.Model):
    name = models.CharField('Название', max_length=255)

    def __unicode__(self):
        return f'<Специализация: {self.name}>'

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'


class Tags(models.Model):
    name = models.CharField('Название', max_length=255)
    perks = models.ManyToManyField('Perks', related_name='tags')

    def __unicode__(self):
        return f'<Тег: {self.name}>'

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

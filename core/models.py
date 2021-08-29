from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perk(models.Model):
    name = models.CharField('Название', max_length=255)
    tag_level_sum = models.FloatField('Сумма соответствия тегов')

    def __str__(self):
        return f'<Специализация: {self.name}>'

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'


class Tag(models.Model):
    name = models.CharField('Название', max_length=255)
    perks = models.ManyToManyField('Perk', related_name='tags', blank=True)

    def __str__(self):
        return f'<Тег: {self.name}>'

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class TagPerk(models.Model):
    perk = models.ForeignKey('Perk', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    level = models.FloatField('Соответствие')


# @receiver(post_save, sender=TagPerk)
# def set_username(created, instance, **kwargs):
#     if created:
#         instance.perk.tag_level_sum += instance.level
#         Avg()

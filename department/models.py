from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=255)
    parent = models.ForeignKey('self', verbose_name='Родительский департамент', on_delete=models.CASCADE,
                               related_name='children', null=True, default=None)

    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'департаменты'

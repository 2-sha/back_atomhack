from django.db import models


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=255, blank=True)
    text = models.TextField('Содержание')
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, related_name='tasks',
                                   null=True, blank=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    specializations = models.ManyToManyField('core.Specialization', related_name='tasks')

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

from django.db import models


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=255, blank=True)
    text = models.TextField('Содержание')
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, related_name='tasks',
                                   null=True, blank=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    tags = models.ManyToManyField('core.Tags', related_name='tasks', blank=True)

    def __str__(self):
        return f'<Задача: {self.title}>'

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=255, blank=True)
    text = models.TextField('Содержание')
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, related_name='tasks',
                                   null=True, blank=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    tags = models.ManyToManyField('core.Tag', related_name='tasks', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


@receiver(pre_save, sender=Task)
def set_department(sender, instance, **kwargs):
    if instance and not instance.department and instance.user and instance.user.department:
        instance.department = instance.user.department

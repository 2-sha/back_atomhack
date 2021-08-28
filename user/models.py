from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.EmailField('Почта', max_length=255)
    phone = models.CharField('Телефон', max_length=255, blank=True)
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, related_name='users',
                                   null=True, blank=True)
    specializations = models.ManyToManyField('core.Specialization', through='UserSpecialization', related_name='users')
    kpi = models.IntegerField('Общая эффективность')


class UserSpecialization(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    abilities = models.ForeignKey('core.Specialization', on_delete=models.CASCADE)
    effectivity = models.IntegerField('Эффективность')

    class Meta:
        verbose_name = 'способность пользователя'
        verbose_name_plural = 'способности пользователя'

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

import random
from unidecode import unidecode


class User(AbstractUser):
    phone = models.CharField('Телефон', max_length=255, blank=True)
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, related_name='users',
                                   null=True, blank=True, verbose_name='Департамент')
    position = models.CharField('Должность', max_length=255, blank=True)
    max_slots = models.IntegerField('Максмальное кол-во задач', default=6)
    perks = models.ManyToManyField('core.Perk', verbose_name='Способности', through='UserPerk', related_name='users')
    kpi = models.FloatField('Общая эффективность', default=0.5)

    @property
    def name(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def workload(self):
        if self.tasks.count():
            tasks = self.tasks.count()
        else:
            return 0
        return round(tasks / self.max_slots, 2)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    fname, lname = unidecode(instance.first_name.lower()), unidecode(instance.last_name.lower())
    fname, lname = slugify(fname)[:20], slugify(lname)[:20]
    slug = '{}.{}'.format(fname[:1], lname)
    j = 2
    while User.objects.filter(username=slug).exists():
        if len(fname) > j:
            slug = '{}.{}'.format(fname[:j], lname)
            j += 1
        else:
            random_word = random_syllable() + random_syllable()
            slug = '{}.{}'.format(lname, random_word)
    if not instance.username:
        instance.username = slug


class UserPerk(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    perk = models.ForeignKey('core.Perk', on_delete=models.CASCADE)
    level = models.FloatField('Эффективность')

    def __unicode__(self):
        return f'<Эффективность: {self.user} в {self.perk}>'

    class Meta:
        verbose_name = 'способность пользователя'
        verbose_name_plural = 'способности пользователя'


en_vowel_frequency = [
    ('a', 82), ('e', 127), ('i', 70), ('o', 75), ('u', 27), ('y', 20),
]
en_consonant_frequency = [
    ('b', 15), ('c', 28), ('d', 43), ('f', 22), ('g', 20), ('h', 61), ('j', 1), ('k', 7), ('l', 40),
    ('m', 24), ('n', 68), ('p', 19), ('q', 1), ('r', 60), ('s', 63), ('t', 90), ('v', 10), ('w', 24),
    ('x', 1), ('z', 1),
]


def random_letter(is_vowel):
    if is_vowel:
        letters = en_vowel_frequency
        num = random.randint(1, 401)
    else:
        letters = en_consonant_frequency
        num = random.randint(1, 598)

    counter = 0
    for letter in letters:
        if counter <= num <= counter + letter[1]:
            return letter[0]
        counter += letter[1]
    return '*'


def random_syllable():
    case = random.randint(0, 2)
    syllable = ""
    if case == 0:
        syllable = random_letter(True) + random_letter(False)
    if case == 1:
        syllable = random_letter(False) + random_letter(True)
    if case == 2:
        syllable = random_letter(False) + random_letter(True) + random_letter(False)
    return syllable

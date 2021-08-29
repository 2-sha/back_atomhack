from django.core.management.base import BaseCommand
from django.db.models import Count, F

from faker import Faker
from random import randint

from tasks.models import Task
from core.models import Tag
from user.models import User


class Command(BaseCommand):
    help = 'Генерирует задачи и распределяет их по сотрудникам'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--num',
            type=int,
            help='Кол-во задач',
        )
        parser.add_argument(
            '-t',
            '--tags',
            help='Проставить теги',
            action='store_true'
        )
        parser.add_argument(
            '-a',
            '--assign',
            help='Назначить',
            action='store_true'
        )

    def handle(self, *args, **options):
        fake = Faker(['ru-RU'])
        tags_num = Tag.objects.count()
        users_num = User.objects.count()

        for i in range(options.get('num')):
            task = Task(title=fake.text(60), text=fake.text(300))
            task.save()

            if options.get('tags') and tags_num:
                for j in range(min(tags_num, 5)):
                    task.tags.add(Tag.objects.all()[randint(0, tags_num - 1)])

            if options.get('assign') and users_num:
                # Назначаем задачу любому из 10 самых свободных
                user = User.objects.all()\
                    .annotate(num_tasks=Count('tasks'))\
                    .filter(num_tasks__lte=F('max_slots'))\
                    .order_by('num_tasks')
                if user.exists():
                    task.user = user[randint(0, min(users_num, 10))]
                    task.save(update_fields=['user', 'department'])

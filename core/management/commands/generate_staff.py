from django.core.management.base import BaseCommand
from django.db.models import Count, Q

from russian_names import RussianNames
import phonenumbers
import random
import string
from faker import Faker
from faker.providers.phone_number.en_US import Provider

from user.models import User
from department.models import Department


class CustomPhoneProvider(Provider):
    def phone_number(self):
        while True:
            phone_number = self.numerify(self.random_element(self.formats))
            parsed_number = phonenumbers.parse(phone_number, 'US')
            if phonenumbers.is_valid_number(parsed_number):
                return phonenumbers.format_number(
                    parsed_number,
                    phonenumbers.PhoneNumberFormat.E164
                )


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


class Command(BaseCommand):
    help = 'Генерирует сортрудников и распределяет их по департаментам'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--num',
            type=int,
            help='Кол-во сотрудников',
        )
        parser.add_argument(
            '-a',
            '--assign',
            help='Прикрепить сотрудников к отделам',
            action='store_true'
        )

    def handle(self, *args, **options):
        it = RussianNames(count=options.get('num'), patronymic=False)
        fake = Faker()
        fake.add_provider(CustomPhoneProvider)
        department_num = Department.objects.count() - 1
        for name in it:
            first_name, last_name = name.split(' ')
            user = User(first_name=first_name, last_name=last_name, phone=fake.phone_number(),
                        email=f'{random_char(7)}@mail.ru')
            if options.get('assign') and department_num:
                user.department = Department.objects.all().exclude(Q(parent__isnull=True) | Q(parent__parent__isnull=True))\
                    .annotate(num_users=Count('users')).order_by('num_users').first()
            user.save()

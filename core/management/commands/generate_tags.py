from django.core.management.base import BaseCommand

from random import randint
from pathlib import Path
from os.path import join

from core.models import Tag


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--num',
            type=int,
            help='Кол-во тегов',
        )

    def handle(self, *args, **options):
        BASE_DIR = Path(__file__).resolve().parent
        with open(join(BASE_DIR, 'word_rus.txt'), 'r', encoding='utf-8') as f:
            words = f.read().split('\n')
        words_num = len(words)

        for i in range(options.get('num')):
            Tag.objects.create(name=words[randint(0, words_num)])

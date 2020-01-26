from Teacher.models import Teacher
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create random teacher'

    def add_arguments(self, parser):
        parser.add_argument(
            'total',
            type=int,
            help='Indicates the number of teacher to be created'
        )

    def handle(self, **kwargs):
        total = kwargs['total']

        for _ in range(total):
            Teacher.generate_teacher()

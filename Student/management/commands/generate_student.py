from Student.models import Student
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create random student'

    def add_arguments(self, parser):
        parser.add_argument(
            'total',
            type=int,
            help='Indicates the number of students to be created')

    def handle(self, **kwargs):
        total = kwargs['total']

        for _ in range(total):
            Student.generate_Student()

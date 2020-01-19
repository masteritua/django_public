import random
from Student.models import Student
from Group.models import Group
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

        Group.objects.all().delete()
        Student.objects.all().delete()

        groups = [Group.objects.create(last_name=f'name_{i}') for i in range(10)]

        for _ in range(total):
            student = Student.generate_Student()
            student.group = random.choice(groups)
            student.save()

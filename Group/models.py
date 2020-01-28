from django.db import models
from faker import Faker
from random import randrange
from Teacher.models import Teacher
from Student.models import Student


class Group(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    teacher = models.ForeignKey(
        Teacher, blank=True, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "group"

    def get_curator(self):
        return f'{self.teacher.first_name} {self.teacher.last_name}  {self.teacher.email}'

    def get_leader_class(self):
        return f'{self.student.first_name} {self.student.last_name}  {self.student.email}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    @classmethod
    def generate_group(cls):
        myFactory = Faker()
        name = myFactory.name()
        arr = name.split(' ')

        first_name = arr[0]
        last_name = arr[1]
        email = myFactory.email()

        teacher = Teacher.objects.all().order_by('?').first()
        student = Student.objects.all().order_by('?').first()

        group = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            teacher=teacher,
            student=student,
        )

        group.save()
        return group


def __str__(self):
    return self.get_info()

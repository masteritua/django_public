from django.db import models
from faker import Faker
from random import randrange
from Teacher.models import Teacher
from Student.models import Student


class Group(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    teacher_id = models.ForeignKey(
        Teacher, blank=True, null=True, on_delete=models.CASCADE)
    student_id = models.ForeignKey(
        Student, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "group"

    def get_curator(self):
        return f'{self.teacher_id.first_name} {self.teacher_id.last_name}  {self.teacher_id.email}'

    def get_leader_class(self):
        return f'{self.student_id.first_name} {self.student_id.last_name}  {self.student_id.email}'

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
        teacher_id = randrange(100)
        student_id = randrange(100)

        instanceTeacher = Teacher.objects.get(pk=teacher_id)
        instanceStudent = Student.objects.get(pk=student_id)

        group = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            teacher_id=instanceTeacher,
            student_id=instanceStudent,
        )

        group.save()
        return group

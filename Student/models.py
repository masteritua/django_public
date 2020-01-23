from django.db import models
from faker import Faker


class Student(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "student"

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    @classmethod
    def generate_Student(cls):
        myFactory = Faker()
        name = myFactory.name()
        arr = name.split(' ')

        first_name = arr[0]
        last_name = arr[1]
        email = myFactory.email()

        student = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        student.save()
        return student
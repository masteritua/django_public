from django.db import models
from datetime import datetime
from faker import Faker


class Group(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()

    @classmethod
    def generate_student(cls):
        myFactory = Faker()
        name = myFactory.name()
        arr = name.split(' ')

        first_name = arr[0]
        last_name = arr[1]
        birth_date = myFactory.date(pattern="%Y-%m-%d", end_datetime=None)

        student = cls(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
        )

        student.save()

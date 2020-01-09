from django.db import models
from datetime import datetime
from faker import Faker


class Teacher(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()

    class Meta:
        db_table = "teacher"

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_teacher(cls):
        myFactory = Faker()
        name = myFactory.name()
        arr = name.split(' ')

        first_name = arr[0]
        last_name = arr[1]
        birth_date = myFactory.date(pattern="%Y-%m-%d", end_datetime=None)

        group = cls(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
        )

        group.save()
        return group

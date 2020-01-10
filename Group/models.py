from django.db import models
from datetime import datetime
from faker import Faker


class Group(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "group"

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

        group = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        group.save()
        return group

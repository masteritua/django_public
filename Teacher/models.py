from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, unique=True)

    class Meta:
        db_table = "teacher"

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    @classmethod
    def generate_teacher(cls):
        myFactory = Faker()
        name = myFactory.name()
        arr = name.split(' ')

        first_name = arr[0]
        last_name = arr[1]
        email = myFactory.email()

        teacher = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        teacher.save()
        return teacher

    def __str__(self):
        return self.get_info()



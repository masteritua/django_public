from django.db import models
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12, unique=True)

    class Meta:
        db_table = "student"

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    @classmethod
    def generate_student(cls):
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

    def __str__(self):
        return self.get_info()


class Logger(models.Model):
    path = models.CharField(max_length=100)
    method = models.IntegerField(2)
    time_delta = models.DecimalField(max_digits=5, decimal_places=3)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Logger"

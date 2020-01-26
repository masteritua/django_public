from django.db import models
from faker import Faker


class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # group = models.ForeignKey(
    #     Group, blank=True, null=True, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.get_info()


    def save(self, *args, **kwargs):
        # pre save
        super().save(*args, **kwargs)
        # post save
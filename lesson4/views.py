from .models import Group
from django.http import HttpResponse


def generate_student(request):
    Group.generate_student()
    return HttpResponse("Запись сгенерирована!")

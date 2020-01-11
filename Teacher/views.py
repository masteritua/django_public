from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from Teacher.models import Teacher


def teacher(request):
    queryset = Teacher.objects.all()
    response = ""

    fltr = request.GET

    if len(fltr):
        queryset = queryset.filter(
            Q(first_name__contains=fltr.get('first_name')) |
            Q(last_name__contains=fltr.get('last_name')) |
            Q(email__contains=fltr.get('email'))
        )

    for teacher in queryset:
        response += teacher.get_info() + "<br>"

    return render(request, 'teacher_list.html', context={'teacher_list': response})

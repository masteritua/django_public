from django.shortcuts import render
# Create your views here.
from Teacher.models import Teacher


def teacher(request):
    queryset = Teacher.objects.all()
    response = ""

    fn = request.GET.get('first_name')

    if fn:
        # LIKE %{}%
        queryset.filter(first_name__contains=fn)

    ln = request.GET.get('last_name')

    if ln:
        # LIKE %{}%
        queryset.filter(last_name__contains=ln)

    for teacher in queryset:
        response += teacher.get_info() + "<br>"

    return render(request, 'teacher_list.html', context={'teacher_list': response})

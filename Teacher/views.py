from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from Teacher.models import Teacher
from Teacher.forms import TeacherAddForm, TeacherEditForm, TeacherListForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from common.functions import email
from django.shortcuts import get_object_or_404


def teacher(request):
    queryset = Teacher.objects.all()
    form = TeacherListForm()
    response = ""

    fltr = request.GET

    if len(fltr):
        queryset = queryset.filter(
            Q(first_name__contains=fltr.get('first_name')) |
            Q(last_name__contains=fltr.get('last_name')) |
            Q(email__contains=fltr.get('email'))
        )

    return render(request, 'teacher_list.html',
                  context={
                      'form': form,
                      'teacher_list': response,
                      'queryset': queryset
                  })


def teacher_add(request):
    post = request.POST

    if request.method == 'POST':

        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()

            email(f"Создание сообщения",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse('teacher'))

    else:
        form = TeacherAddForm(initial=post)

    return render(request, 'teacher_add.html', context={"form": form})


def teacher_edit(request, pk):
    instance = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':

        post = request.POST

        form = TeacherEditForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            email(f"Редактирование сообщения № {pk}",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse(teacher))

    else:
        form = TeacherEditForm(instance=instance)

    return render(request, 'teacher_edit.html', context={
        "form": form,
        "object": instance,
    })

from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from Student.models import Student
from Student.forms import StudentAddForm, StudentEditForm, StudentListForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from common.functions import email


def student(request):
    queryset = Student.objects.all()
    form = StudentListForm()
    response = ""

    fltr = request.GET

    if len(fltr):
        queryset = queryset.filter(
            Q(first_name__contains=fltr.get('first_name')) |
            Q(last_name__contains=fltr.get('last_name')) |
            Q(email__contains=fltr.get('email'))
        )

    return render(request, 'student_list.html',
                  context={
                      'form': form,
                      'Student_list': response,
                      'queryset': queryset
                  })


def student_add(request):

    post = request.POST

    if request.method == 'POST':

        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()

            email(f"Создание сообщения",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse('student'))

    else:
        form = StudentAddForm(initial=post)

    return render(request, 'student_add.html', context={"form": form})


def student_edit(request, pk):

    instance = Student.objects.get(pk=pk)

    if request.method == 'POST':

        post = request.POST

        form = StudentEditForm(request.POST, instance=instance)

        if form.is_valid():
            form.first_name = post.get('first_name')
            form.last_name = post.get('last_name')
            form.email = post.get('email')
            form.save()

            email(f"Редактирование сообщения № {pk}",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse(student))

    else:
        form = StudentEditForm(
            initial={
                'first_name': instance.first_name,
                'last_name': instance.last_name,
                'email': instance.email
            })

    return render(request, 'student_edit.html', context={
        "form": form,
        'object': instance
    })

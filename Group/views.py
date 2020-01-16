from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from Group.models import Group
from Group.forms import GroupAddForm, GroupEditForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from common.functions import email


def group(request):
    queryset = Group.objects.all()
    response = ""

    fltr = request.GET

    if len(fltr):
        queryset = queryset.filter(
            Q(first_name__contains=fltr.get('first_name')) |
            Q(last_name__contains=fltr.get('last_name')) |
            Q(email__contains=fltr.get('email'))
        )

    return render(request, 'group_list.html',
                  context={
                      'group_list': response,
                      'queryset': queryset
                  })


def group_add(request):
    if request.method == 'POST':

        post = request.POST

        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()

            email(f"Создание сообщения",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse('group'))

    else:
        form = GroupAddForm()

    return render(request, 'group_add.html', context={"form": form})


def group_edit(request, pk):
    o = Group.objects.get(pk=pk)

    if request.method == 'POST':

        post = request.POST

        form = GroupEditForm(request.POST)

        if form.is_valid():
            o.first_name = post.get('first_name')
            o.last_name = post.get('last_name')
            o.email = post.get('email')
            o.save()

            email(f"Редактирование сообщения № {pk}",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse(group))

    else:
        form = GroupEditForm()

    return render(request, 'group_edit.html', context={
        "form": form,
        "object": o,
    })

from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from Group.models import Group
from Group.forms import GroupAddForm, GroupEditForm, GroupListForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from common.functions import email
from django.shortcuts import get_object_or_404


def group(request):
    queryset = Group.objects.select_related('teacher', 'student').all()
    form = GroupListForm()
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
                      'form': form,
                      'group_list': response,
                      'queryset': queryset
                  })


def group_add(request):
    post = request.POST

    if request.method == 'POST':

        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()

            email(f"Создание сообщения",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse('group'))

    else:
        form = GroupAddForm(initial=post)

    return render(request, 'group_add.html', context={"form": form})


def group_edit(request, pk):
    instance = get_object_or_404(Group.objects.select_related('teacher', 'student'), pk=pk)

    if request.method == 'POST':

        post = request.POST

        form = GroupEditForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            email(f"Редактирование сообщения № {pk}",
                  f"{post.get('first_name')} {post.get('last_name')} {post.get('email')}")

            return HttpResponseRedirect(reverse(group))

    else:
        form = GroupEditForm(instance=instance)

    return render(request, 'group_edit.html', context={
        "form": form,
        'object': instance
    })

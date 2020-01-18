from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from Group.models import Group
from Group.forms import GroupAddForm
from django.http import HttpResponseRedirect


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

    for group in queryset:
        response += group.get_info() + "<br>"

    return render(request, 'group_list.html', context={'group_list': response})


def group_add(request):
    if request.method == 'POST':

        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/group')

    else:
        form = GroupAddForm()

    return render(request, 'group_add.html', context={"form": form})

from django.shortcuts import render
# Create your views here.
from Group.models import Group


def group(request):
    queryset = Group.objects.all()
    response = ""

    fn = request.GET.get('first_name')

    if fn:
        # LIKE %{}%
        queryset.filter(first_name__contains=fn)

    ln = request.GET.get('last_name')

    if ln:
        # LIKE %{}%
        queryset.filter(last_name__contains=ln)

    for group in queryset:
        response += group.get_info() + "<br>"

    return render(request, 'group_list.html', context={'group_list': response})

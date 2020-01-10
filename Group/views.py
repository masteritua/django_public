from django.shortcuts import render
# Create your views here.
from Group.models import Group


def group(request):
    queryset = Group.objects.all()
    response = ""

    fltr = request.GET.get('filter')

    if fltr:
        queryset = queryset.filter(Q(first_name__contains=fltr) |
                                   Q(last_name__contains=fltr) | Q(email__contains=fltr))

    for group in queryset:
        response += group.get_info() + "<br>"

    return render(request, 'group_list.html', context={'group_list': response})

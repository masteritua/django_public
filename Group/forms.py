from django.forms import ModelForm
from Group.models import Group


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class GroupEditForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

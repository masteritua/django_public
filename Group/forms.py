from django.forms import ModelForm
from Group.models import Group


class GroupListForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class GroupEditForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

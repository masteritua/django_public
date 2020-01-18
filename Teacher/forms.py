from django.forms import ModelForm
from Teacher.models import Teacher


class TeacherListForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherEditForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

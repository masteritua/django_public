from django.forms import ModelForm
from Teacher.models import Teacher


class TeacherAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherEditForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

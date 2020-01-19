from django.forms import ModelForm
from Student.models import Student


class StudentListForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentEditForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

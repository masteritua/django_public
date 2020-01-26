from django.forms import ModelForm, ValidationError
from Student.models import Student


class BaseStudentForm(ModelForm):
    def clean_email(self):

        email = self.cleaned_data['email'].lower()

        email_exists = Student.objects\
            .filter(email__iexact=email)\
            .exclude(email__iexact=self.instance.email).exists()

        # self.instance.email
    #     if Student.objects.filter(email__iexact=email).exists():
    #         raise ValidationError(f'{email} is already used!')
    #     return email
        pass


class StudentListForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentEditForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name')

from django.forms import ModelForm
from Teacher.models import Teacher
from django.forms import ValidationError


class BaseTeacherForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Teacher.objects \
            .filter(email__iexact=email) \
            .exclude(id=self.instance.id)

        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone'].lower()

        if not phone.isdigit():
            raise ValidationError(f'Поле {phone} должно состоять только из цифр')

        return phone

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        return first_name.title()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        return last_name.title()


class TeacherListForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherEditForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherAdminForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = "__all__"

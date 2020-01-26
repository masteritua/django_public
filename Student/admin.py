from django.contrib import admin
from Student.models import Student
from Student.forms import StudentAdminForm


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_per_page = 10
    form = StudentAdminForm


admin.site.register(Student, StudentAdmin)

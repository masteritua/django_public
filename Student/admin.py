from django.contrib import admin
from Student.models import Student
from Group.admin import GroupAdminInline
from Student.forms import StudentAdminForm


class StudentAdmin(admin.ModelAdmin):
    inlines = (GroupAdminInline,)
    form = StudentAdminForm


admin.site.register(Student, StudentAdmin)

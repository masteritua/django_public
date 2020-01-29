from django.contrib import admin
from Student.models import Student
from Group.admin import GroupAdminInline


class StudentAdmin(admin.ModelAdmin):
    inlines = (GroupAdminInline,)


admin.site.register(Student, StudentAdmin)

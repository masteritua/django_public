from django.contrib import admin
from Teacher.models import Teacher
from Group.admin import GroupAdminInline


class TeacherAdmin(admin.ModelAdmin):
    inlines = (GroupAdminInline,)


admin.site.register(Teacher, TeacherAdmin)

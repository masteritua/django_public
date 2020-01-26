from django.contrib import admin
from Teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)

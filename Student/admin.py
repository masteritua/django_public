from django.contrib import admin
from Student.models import Student


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)

from django.contrib import admin
from Teacher.models import Teacher
from Group.admin import GroupAdminInline
from Teacher.forms import TeacherAdminForm

class TeacherAdmin(admin.ModelAdmin):
    inlines = (GroupAdminInline,)
    form = TeacherAdminForm

admin.site.register(Teacher, TeacherAdmin)

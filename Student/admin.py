from django.contrib import admin
from Student.models import Student


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['email']
    list_display = ('id', 'first_name', 'last_name', 'email')
    #list_select_related = ('Group',) relation

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='admin').exists():
            return('email')
        return ()


admin.site.register(Student, StudentAdmin)
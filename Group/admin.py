from django.contrib import admin
from Group.models import Group
from Group.inlines import StudentInline

class GroupAdmin(admin.ModelAdmin):
   #inlines = [StudentInline, ]
   pass


admin.site.register(Group, GroupAdmin)


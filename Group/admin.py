from django.contrib import admin
from Group.models import Group


class GroupAdminInline(admin.TabularInline):
    model = Group


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)

from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'password')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

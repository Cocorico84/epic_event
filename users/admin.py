from django.contrib import admin
from django.contrib.auth.models import Group


from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username", "email", "is_staff", "category",)
    list_filter = ("last_login",)


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)

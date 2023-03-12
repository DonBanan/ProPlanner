from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'id', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'first_name', 'last_name', 'middle_name')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'middle_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'middle_name', 'email'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
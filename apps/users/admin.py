from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'name',
                'email',
                'gender',
                'birth_date',
                'is_staff',
            )
        }),
    )
    
    list_display = (
        'id',
        'username',
        'name',
        'email',
        'gender',
        'birth_date',
        'date_joined',
        'last_login',
        "is_active",
        "is_staff",
    )
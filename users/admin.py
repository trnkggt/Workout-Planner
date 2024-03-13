from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "first_name",
        "is_staff"
    ]
    ordering = [
        'email',
    ]

admin.site.register(CustomUser, CustomUserAdmin)

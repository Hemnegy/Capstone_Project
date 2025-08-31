from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields shown in the list view
    list_display = ("id", "username", "email", "phone", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "email", "phone")
    ordering = ("username",)

    # Add our custom fields to fieldsets (used in admin detail view)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone", "role")}),
    )

    # Add our custom fields to add_fieldsets (used when creating a new user)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("phone", "role")}),
    )

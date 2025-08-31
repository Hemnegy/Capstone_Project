from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "duration_minutes", "price")
    search_fields = ("name",)
    list_filter = ("duration_minutes",)
    ordering = ("name",)

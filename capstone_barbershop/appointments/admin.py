from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'barber', 'service', 'date', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'date', 'barber')
    search_fields = ('customer__username', 'barber__user__username', 'service__name')
    ordering = ('-date', '-start_time')

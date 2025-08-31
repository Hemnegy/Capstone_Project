from django.contrib import admin
from .models import BarberProfile, Availability


@admin.register(BarberProfile)
class BarberProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'specialty', 'experience_years')
    search_fields = ('user__username', 'specialty')
    list_filter = ('experience_years',)


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'barber', 'date', 'start_time', 'end_time')
    search_fields = ('barber__user__username',)
    list_filter = ('date',)
    ordering = ('-date', 'start_time')

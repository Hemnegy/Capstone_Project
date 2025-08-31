from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users (auth, register, login)
    path('api/users/', include('users.urls')),

    # Barbers & availability
    path('api/barbers/', include('barbers.urls')),

    # Services
    path('api/services/', include('services.urls')),

    # Appointments
    path('api/appointments/', include('appointments.urls')),
]

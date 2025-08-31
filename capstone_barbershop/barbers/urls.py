# barbers/urls.py
from django.urls import path
from .views import (
    BarberProfileListView, BarberProfileDetailView, BarberProfileCreateUpdateView,
    AvailabilityListCreateView, AvailabilityDetailView
)

urlpatterns = [
    path('', BarberProfileListView.as_view(), name='barber-list'),
    path('<int:pk>/', BarberProfileDetailView.as_view(), name='barber-detail'),
    path('me/', BarberProfileCreateUpdateView.as_view(), name='barber-me'),
    path('availability/', AvailabilityListCreateView.as_view(), name='availability-list-create'),
    path('availability/<int:pk>/', AvailabilityDetailView.as_view(), name='availability-detail'),
]

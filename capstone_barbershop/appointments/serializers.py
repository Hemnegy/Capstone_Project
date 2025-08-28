# appointments/serializers.py
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    customer_username = serializers.ReadOnlyField(source='customer.username')
    barber_username = serializers.ReadOnlyField(source='barber.user.username')
    service_name = serializers.ReadOnlyField(source='service.name')

    class Meta:
        model = Appointment
        fields = [
            'id', 'customer', 'customer_username',
            'barber', 'barber_username',
            'service', 'service_name',
            'date', 'start_time', 'end_time', 'status'
        ]

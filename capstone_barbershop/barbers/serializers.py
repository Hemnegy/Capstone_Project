# barbers/serializers.py
from rest_framework import serializers
from .models import BarberProfile, Availability

class BarberProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = BarberProfile
        fields = ['id', 'user', 'username', 'email', 'specialty', 'experience_years']
        read_only_fields = ['user']   # user is auto-linked on create


class AvailabilitySerializer(serializers.ModelSerializer):
    barber_name = serializers.ReadOnlyField(source='barber.user.username')

    class Meta:
        model = Availability
        fields = ['id', 'barber', 'barber_name', 'date', 'start_time', 'end_time']

from django.db import models
from users.models import User

class BarberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='barber_profile')
    specialty = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

class Availability(models.Model):
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.barber.user.username} - {self.date}"

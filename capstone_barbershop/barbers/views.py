# barbers/views.py
from rest_framework import generics, permissions
from .models import BarberProfile, Availability
from .serializers import BarberProfileSerializer, AvailabilitySerializer

# --- Barber Profile Views ---
class BarberProfileListView(generics.ListAPIView):
    queryset = BarberProfile.objects.all()
    serializer_class = BarberProfileSerializer
    permission_classes = [permissions.AllowAny]   # anyone can view


class BarberProfileDetailView(generics.RetrieveAPIView):
    queryset = BarberProfile.objects.all()
    serializer_class = BarberProfileSerializer
    permission_classes = [permissions.AllowAny]


class BarberProfileCreateUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BarberProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # ensure barber only edits their own profile
        return self.request.user.barber_profile


# --- Availability Views ---
class AvailabilityListCreateView(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Customers can filter by ?date=YYYY-MM-DD&barber_id=1
        queryset = Availability.objects.all()
        date = self.request.query_params.get("date")
        barber_id = self.request.query_params.get("barber_id")
        if date:
            queryset = queryset.filter(date=date)
        if barber_id:
            queryset = queryset.filter(barber_id=barber_id)
        return queryset

    def perform_create(self, serializer):
        # only barbers can add their availability
        serializer.save(barber=self.request.user.barber_profile)


class AvailabilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

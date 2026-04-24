from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from core.shared.permissions import IsDoctor, IsPatient


class AppointmentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing appointments."""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Filter by patient or doctor
        user = self.request.user
        if hasattr(user, 'patient'):
            return Appointment.objects.filter(patient__user=user)
        elif hasattr(user, 'doctor'):
            return Appointment.objects.filter(doctor__user=user)
        return Appointment.objects.all()

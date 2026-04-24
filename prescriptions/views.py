from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Prescription
from .serializers import PrescriptionSerializer
from core.shared.permissions import IsDoctor, IsPatient


class PrescriptionViewSet(viewsets.ModelViewSet):
    """ViewSet for managing prescriptions."""
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return Prescription.objects.filter(patient__user=user)
        elif hasattr(user, 'doctor'):
            return Prescription.objects.filter(doctor__user=user)
        return Prescription.objects.all()

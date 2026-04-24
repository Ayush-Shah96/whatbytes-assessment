from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    """ViewSet for managing medical records."""
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return MedicalRecord.objects.filter(patient__user=user)
        elif hasattr(user, 'doctor'):
            return MedicalRecord.objects.filter(doctor__user=user)
        return MedicalRecord.objects.all()

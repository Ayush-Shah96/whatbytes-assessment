from rest_framework import serializers
from .models import Prescription, PrescriptionItem


class PrescriptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItem
        fields = ['id', 'medication', 'dosage', 'frequency', 'duration_days', 'quantity', 'instructions']


class PrescriptionSerializer(serializers.ModelSerializer):
    items = PrescriptionItemSerializer(many=True, read_only=True)
    patient_name = serializers.CharField(source='patient.user.get_full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.user.get_full_name', read_only=True)
    
    class Meta:
        model = Prescription
        fields = [
            'id', 'patient', 'patient_name', 'doctor', 'doctor_name',
            'appointment', 'issue_date', 'expiry_date', 'status',
            'notes', 'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'issue_date', 'created_at', 'updated_at']

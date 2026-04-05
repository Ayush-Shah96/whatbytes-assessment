from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """Serializer for creating and reading patient-doctor mappings."""

    # Nested read-only representations
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    doctor_specialization = serializers.CharField(
        source='doctor.get_specialization_display',
        read_only=True
    )
    assigned_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'patient_name', 'doctor', 'doctor_name',
            'doctor_specialization', 'notes', 'assigned_by', 'assigned_at'
        ]
        read_only_fields = ['id', 'assigned_by', 'assigned_at']

    def validate(self, attrs):
        """Ensure the patient-doctor pair doesn't already exist."""
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError(
                {
                    "non_field_errors": (
                        f"Dr. {doctor.name} is already assigned to patient {patient.name}."
                    )
                }
            )
        return attrs


class PatientDoctorMappingDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for mappings with full nested objects."""

    from patients.serializers import PatientListSerializer
    from doctors.serializers import DoctorListSerializer

    patient_detail = serializers.SerializerMethodField()
    doctor_detail = serializers.SerializerMethodField()
    assigned_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'patient_detail', 'doctor', 'doctor_detail',
            'notes', 'assigned_by', 'assigned_at'
        ]

    def get_patient_detail(self, obj):
        from patients.serializers import PatientListSerializer
        return PatientListSerializer(obj.patient).data

    def get_doctor_detail(self, obj):
        from doctors.serializers import DoctorListSerializer
        return DoctorListSerializer(obj.doctor).data


class DoctorsByPatientSerializer(serializers.ModelSerializer):
    """Serializer to show doctors assigned to a specific patient."""

    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    doctor_specialization = serializers.CharField(
        source='doctor.get_specialization_display',
        read_only=True
    )
    doctor_phone = serializers.CharField(source='doctor.phone', read_only=True)
    doctor_email = serializers.EmailField(source='doctor.email', read_only=True)
    doctor_hospital = serializers.CharField(
        source='doctor.hospital_affiliation',
        read_only=True
    )
    doctor_available = serializers.BooleanField(source='doctor.available', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'doctor', 'doctor_name', 'doctor_specialization',
            'doctor_phone', 'doctor_email', 'doctor_hospital',
            'doctor_available', 'notes', 'assigned_at'
        ]

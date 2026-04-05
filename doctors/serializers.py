from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """Full serializer for Doctor model."""

    created_by = serializers.StringRelatedField(read_only=True)
    specialization_display = serializers.CharField(
        source='get_specialization_display',
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'specialization', 'specialization_display',
            'license_number', 'years_of_experience', 'qualification',
            'email', 'phone', 'hospital_affiliation', 'available',
            'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def validate_license_number(self, value):
        """Ensure license number is alphanumeric and non-empty."""
        value = value.strip()
        if not value:
            raise serializers.ValidationError("License number cannot be blank.")
        return value.upper()

    def validate_years_of_experience(self, value):
        if value < 0 or value > 70:
            raise serializers.ValidationError(
                "Years of experience must be between 0 and 70."
            )
        return value

    def validate_phone(self, value):
        cleaned = ''.join(filter(str.isdigit, value))
        if len(cleaned) < 7 or len(cleaned) > 15:
            raise serializers.ValidationError(
                "Enter a valid phone number (7-15 digits)."
            )
        return value


class DoctorListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing doctors."""

    specialization_display = serializers.CharField(
        source='get_specialization_display',
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'specialization', 'specialization_display',
            'hospital_affiliation', 'available', 'created_at'
        ]

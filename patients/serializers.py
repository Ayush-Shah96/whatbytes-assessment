from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for Patient model."""
    
    age = serializers.ReadOnlyField()
    created_by = serializers.StringRelatedField(read_only=True)
    gender_display = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )
    blood_group_display = serializers.CharField(
        source='get_blood_group_display',
        read_only=True
    )

    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'date_of_birth', 'age', 'gender', 'gender_display',
            'email', 'phone', 'address', 'blood_group', 'blood_group_display',
            'medical_history', 'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def validate_date_of_birth(self, value):
        """Ensure date of birth is not in the future."""
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError(
                "Date of birth cannot be in the future."
            )
        return value

    def validate_phone(self, value):
        """Basic phone number validation."""
        if value:
            cleaned = ''.join(filter(str.isdigit, value))
            if len(cleaned) < 7 or len(cleaned) > 15:
                raise serializers.ValidationError(
                    "Enter a valid phone number (7-15 digits)."
                )
        return value


class PatientListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing patients."""
    
    age = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'age', 'gender', 'phone', 'created_at']

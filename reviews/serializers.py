from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(source='reviewer.user.get_full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.user.get_full_name', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'reviewer', 'reviewer_name', 'doctor', 'doctor_name',
            'appointment', 'rating', 'comment', 'is_verified', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'is_verified']

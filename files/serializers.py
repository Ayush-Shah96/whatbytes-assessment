from rest_framework import serializers
from .models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    uploader_name = serializers.CharField(source='uploaded_by.get_full_name', read_only=True)
    
    class Meta:
        model = FileUpload
        fields = [
            'id', 'file', 'original_filename', 'file_type', 'file_size',
            'uploaded_by', 'uploader_name', 'patient', 'uploaded_at'
        ]
        read_only_fields = ['id', 'file_size', 'uploaded_at']

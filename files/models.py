from django.db import models
from django.contrib.auth.models import User


class FileUpload(models.Model):
    """File upload model."""
    
    FILE_TYPE_CHOICES = [
        ('prescription', 'Prescription'),
        ('report', 'Report'),
        ('image', 'Image'),
        ('document', 'Document'),
        ('other', 'Other'),
    ]
    
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    original_filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    file_size = models.BigIntegerField()  # in bytes
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.original_filename

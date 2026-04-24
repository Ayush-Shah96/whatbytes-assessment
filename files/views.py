from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import FileUpload
from .serializers import FileUploadSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    """ViewSet for managing file uploads."""
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated]

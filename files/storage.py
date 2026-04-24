"""File storage and management utilities."""

import os
from django.conf import settings


def get_upload_path(instance, filename):
    """Generate upload path for files."""
    return f"uploads/{instance.file_type}/{instance.patient.id}/{filename}"


def validate_file_size(file, max_size_mb=50):
    """Validate file size."""
    max_size_bytes = max_size_mb * 1024 * 1024
    return file.size <= max_size_bytes


def validate_file_type(filename, allowed_types):
    """Validate file type."""
    ext = os.path.splitext(filename)[1].lower()
    return ext in allowed_types

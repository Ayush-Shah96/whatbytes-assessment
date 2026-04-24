from django.contrib import admin
from .models import FileUpload


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_by', 'file_type', 'file_size', 'uploaded_at']
    list_filter = ['file_type', 'uploaded_at']
    search_fields = ['uploaded_by__username', 'original_filename']
    readonly_fields = ['uploaded_at', 'file_size']

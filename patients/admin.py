from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_of_birth', 'gender', 'phone', 'created_by', 'created_at']
    list_filter = ['gender', 'blood_group', 'created_at']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

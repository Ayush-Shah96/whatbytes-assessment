from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specialization', 'license_number', 'hospital_affiliation', 'available', 'created_at']
    list_filter = ['specialization', 'available', 'created_at']
    search_fields = ['name', 'email', 'license_number', 'hospital_affiliation']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

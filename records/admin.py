from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'record_type', 'created_at']
    list_filter = ['record_type', 'created_at']
    search_fields = ['patient__user__username']
    readonly_fields = ['created_at', 'updated_at']

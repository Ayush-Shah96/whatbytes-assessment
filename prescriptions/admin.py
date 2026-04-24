from django.contrib import admin
from .models import Prescription, PrescriptionItem


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['patient__user__username', 'doctor__user__username']


@admin.register(PrescriptionItem)
class PrescriptionItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'prescription', 'medication', 'dosage', 'frequency']
    search_fields = ['prescription__id', 'medication']

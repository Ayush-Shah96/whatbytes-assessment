from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'appointment_time', 'status', 'created_at']
    list_filter = ['status', 'appointment_time', 'created_at']
    search_fields = ['patient__user__username', 'doctor__user__username']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

"""Appointment filters."""

import django_filters
from .models import Appointment


class AppointmentFilter(django_filters.FilterSet):
    """Filter for appointments."""
    status = django_filters.CharFilter(field_name='status')
    appointment_date = django_filters.DateFilter(field_name='appointment_time__date')
    
    class Meta:
        model = Appointment
        fields = ['status', 'doctor', 'patient']

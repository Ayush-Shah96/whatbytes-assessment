"""Appointment utility functions."""

from django.utils import timezone
from datetime import timedelta


def get_available_slots(doctor, date, duration_minutes=30):
    """Get available appointment slots for a doctor on a specific date."""
    from .models import Appointment
    
    # Define working hours: 9 AM to 5 PM
    start_hour = 9
    end_hour = 17
    
    appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_time__date=date,
        status__in=['scheduled', 'confirmed', 'in_progress']
    ).order_by('appointment_time')
    
    slots = []
    current_time = timezone.make_aware(timezone.datetime.combine(date, timezone.datetime.min.time().replace(hour=start_hour)))
    end_time = timezone.make_aware(timezone.datetime.combine(date, timezone.datetime.min.time().replace(hour=end_hour)))
    
    booked_times = set()
    for appointment in appointments:
        booked_times.add(appointment.appointment_time)
    
    while current_time < end_time:
        if current_time not in booked_times:
            slots.append(current_time)
        current_time += timedelta(minutes=duration_minutes)
    
    return slots

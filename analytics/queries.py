"""Analytics query functions."""

from django.db.models import Count, Sum
from appointments.models import Appointment
from billing.models import Invoice


def get_appointment_statistics():
    """Get appointment statistics."""
    return {
        'total': Appointment.objects.count(),
        'completed': Appointment.objects.filter(status='completed').count(),
        'cancelled': Appointment.objects.filter(status='cancelled').count(),
        'by_status': Appointment.objects.values('status').annotate(count=Count('id'))
    }


def get_revenue_statistics():
    """Get revenue statistics."""
    return {
        'total_revenue': Invoice.objects.filter(status='paid').aggregate(Sum('total_amount')),
        'pending_invoices': Invoice.objects.filter(status='sent').count(),
    }

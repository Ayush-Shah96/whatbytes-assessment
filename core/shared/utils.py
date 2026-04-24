"""
Utility functions for the Healthcare system.
"""

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)


def send_email_notification(subject, template_name, context, recipient_list):
    """Send email notification using template."""
    try:
        html_message = render_to_string(f'emails/{template_name}', context)
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            'noreply@healthcare.com',
            recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False


def get_client_ip(request):
    """Get client IP from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def format_phone_number(phone):
    """Format phone number."""
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return f"+1-{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11:
        return f"+{digits[0]}-{digits[1:4]}-{digits[4:7]}-{digits[7:]}"
    return phone


def validate_doctor_availability(doctor, datetime_obj):
    """Check if doctor is available at given datetime."""
    # This would query the doctor's schedule and appointments
    from appointments.models import Appointment
    conflicts = Appointment.objects.filter(
        doctor=doctor,
        appointment_time=datetime_obj,
        status__in=['scheduled', 'in_progress']
    ).exists()
    return not conflicts

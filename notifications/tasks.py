"""Celery tasks for notifications."""

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Notification
from appointments.models import Appointment
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_appointment_reminders():
    """Send appointment reminders 24 hours before."""
    tomorrow = timezone.now() + timedelta(days=1)
    appointments = Appointment.objects.filter(
        appointment_time__date=tomorrow.date(),
        status__in=['scheduled', 'confirmed']
    )
    
    for appointment in appointments:
        # Send email reminder
        send_appointment_reminder_email.delay(appointment.id)
        
        # Create notification
        Notification.objects.create(
            recipient=appointment.patient.user,
            notification_type='reminder',
            title='Appointment Reminder',
            message=f'Your appointment with {appointment.doctor.user.get_full_name()} is tomorrow at {appointment.appointment_time.strftime("%I:%M %p")}'
        )


@shared_task
def send_appointment_reminder_email(appointment_id):
    """Send appointment reminder email."""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        html_message = render_to_string('emails/appointment_reminder.html', {
            'appointment': appointment
        })
        plain_message = strip_tags(html_message)
        send_mail(
            'Appointment Reminder',
            plain_message,
            'noreply@healthcare.com',
            [appointment.patient.user.email],
            html_message=html_message,
        )
    except Appointment.DoesNotExist:
        pass


@shared_task
def send_appointment_confirmation(appointment_id):
    """Send appointment confirmation email."""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        html_message = render_to_string('emails/appointment_confirmation.html', {
            'appointment': appointment
        })
        plain_message = strip_tags(html_message)
        send_mail(
            'Appointment Confirmation',
            plain_message,
            'noreply@healthcare.com',
            [appointment.patient.user.email],
            html_message=html_message,
        )
    except Appointment.DoesNotExist:
        pass

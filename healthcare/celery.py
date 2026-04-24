"""
Celery configuration for Healthcare Backend Project.
"""

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.config.settings.development')

app = Celery('healthcare')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-appointment-reminders': {
        'task': 'notifications.tasks.send_appointment_reminders',
        'schedule': crontab(hour=9, minute=0),
    },
    'generate-billing-invoices': {
        'task': 'billing.tasks.generate_invoices',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),
    },
    'cleanup-temp-files': {
        'task': 'files.tasks.cleanup_temp_files',
        'schedule': crontab(hour=2, minute=0),
    },
}

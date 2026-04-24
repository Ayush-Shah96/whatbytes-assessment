from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    """Notification model."""
    
    NOTIFICATION_TYPE_CHOICES = [
        ('appointment', 'Appointment'),
        ('prescription', 'Prescription'),
        ('bill', 'Billing'),
        ('message', 'Message'),
        ('alert', 'Alert'),
        ('reminder', 'Reminder'),
    ]
    
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    related_id = models.IntegerField(null=True, blank=True)  # ID of related object
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.recipient.username}"

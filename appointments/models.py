from django.db import models
from django.contrib.auth.models import User
from core.shared.models import TimestampedModel, AuditModel


class Appointment(AuditModel):
    """Appointment model for doctor-patient meetings."""
    
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]
    
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='appointments')
    appointment_time = models.DateTimeField()
    duration_minutes = models.IntegerField(default=30)
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-appointment_time']
        unique_together = [['doctor', 'appointment_time']]
    
    def __str__(self):
        return f"Appointment: {self.patient} - {self.doctor} at {self.appointment_time}"

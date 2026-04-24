from django.db import models
from core.shared.models import AuditModel


class Prescription(AuditModel):
    """Prescription model."""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ]
    
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='prescriptions')
    appointment = models.ForeignKey('appointments.Appointment', on_delete=models.SET_NULL, null=True, blank=True)
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"Prescription for {self.patient.user.get_full_name()} by {self.doctor.user.get_full_name()}"


class PrescriptionItem(models.Model):
    """Individual medication in a prescription."""
    
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='items')
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)  # e.g., "500mg"
    frequency = models.CharField(max_length=100)  # e.g., "twice daily"
    duration_days = models.IntegerField()
    quantity = models.IntegerField()
    instructions = models.TextField(blank=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.medication} - {self.dosage}"

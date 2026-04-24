from django.db import models
from core.shared.models import AuditModel


class MedicalRecord(AuditModel):
    """Medical record model."""
    
    RECORD_TYPE_CHOICES = [
        ('consultation', 'Consultation Notes'),
        ('diagnosis', 'Diagnosis'),
        ('lab_test', 'Lab Test Results'),
        ('imaging', 'Imaging Results'),
        ('surgery', 'Surgery Notes'),
        ('discharge', 'Discharge Summary'),
        ('vaccination', 'Vaccination Record'),
        ('allergy', 'Allergy Record'),
        ('other', 'Other'),
    ]
    
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey('appointments.Appointment', on_delete=models.SET_NULL, null=True, blank=True)
    record_type = models.CharField(max_length=20, choices=RECORD_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    findings = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)
    is_confidential = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_record_type_display()} - {self.patient.user.get_full_name()}"

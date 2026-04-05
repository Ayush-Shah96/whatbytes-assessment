from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):
    """
    Model representing the assignment of a doctor to a patient.
    A patient can have multiple doctors; a doctor can have multiple patients.
    """

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='doctor_mappings'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patient_mappings'
    )
    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_mappings',
        help_text="The user who created this assignment."
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Optional notes about this assignment (e.g., reason for referral)."
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # Prevent duplicate mappings
        ordering = ['-assigned_at']
        verbose_name = 'Patient-Doctor Mapping'
        verbose_name_plural = 'Patient-Doctor Mappings'

    def __str__(self):
        return f"{self.patient.name} → Dr. {self.doctor.name}"

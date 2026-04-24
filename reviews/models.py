from django.db import models
from core.shared.models import TimestampedModel


class Review(TimestampedModel):
    """Review and rating model for doctors."""
    
    reviewer = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='reviews_given')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='reviews_received')
    appointment = models.OneToOneField('appointments.Appointment', on_delete=models.SET_NULL, null=True, blank=True)
    
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)  # Verified purchase
    
    class Meta:
        ordering = ['-created_at']
        unique_together = [['reviewer', 'doctor', 'appointment']]
    
    def __str__(self):
        return f"Review by {self.reviewer.user.get_full_name()} for {self.doctor.user.get_full_name()}"

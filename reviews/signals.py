"""Review signals for updating doctor ratings."""

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review


@receiver(post_save, sender=Review)
def update_doctor_rating(sender, instance, created, **kwargs):
    """Update doctor average rating when review is posted."""
    if created:
        # Update the doctor's average rating
        doctor = instance.doctor
        avg_rating = Review.objects.filter(doctor=doctor).aggregate(
            avg_rating=models.Avg('rating')
        )['avg_rating']
        # You would update a rating field on the Doctor model here

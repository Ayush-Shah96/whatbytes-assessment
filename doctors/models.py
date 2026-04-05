from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    """Model representing a doctor record."""

    SPECIALIZATION_CHOICES = [
        ('general', 'General Practitioner'),
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('endocrinology', 'Endocrinology'),
        ('gastroenterology', 'Gastroenterology'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('psychiatry', 'Psychiatry'),
        ('pulmonology', 'Pulmonology'),
        ('radiology', 'Radiology'),
        ('surgery', 'Surgery'),
        ('urology', 'Urology'),
        ('other', 'Other'),
    ]

    # Ownership
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='doctors',
        help_text="The authenticated user who created this doctor record."
    )

    # Professional Information
    name = models.CharField(max_length=255)
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES,
        default='general'
    )
    license_number = models.CharField(
        max_length=100,
        unique=True,
        help_text="Unique medical license number."
    )
    years_of_experience = models.PositiveIntegerField(default=0)
    qualification = models.CharField(
        max_length=255,
        help_text="e.g., MBBS, MD, MS"
    )

    # Contact Information
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    hospital_affiliation = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Hospital or clinic name."
    )

    # Availability
    available = models.BooleanField(default=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return f"Dr. {self.name} - {self.get_specialization_display()}"

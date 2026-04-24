"""
Signals for authentication app.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    """Signal handler when a new user is created."""
    if created:
        # Perform any initialization needed when a new user is created
        pass

"""Audit signals for tracking model changes."""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AuditLog


@receiver(post_save)
def log_object_created(sender, instance, created, **kwargs):
    """Log when an object is created."""
    if created and hasattr(instance, 'created_by'):
        AuditLog.objects.create(
            user=instance.created_by,
            action='create',
            model_name=sender.__name__,
            object_id=instance.id,
            description=f"Created {sender.__name__}: {instance}"
        )


@receiver(post_delete)
def log_object_deleted(sender, instance, **kwargs):
    """Log when an object is deleted."""
    if hasattr(instance, 'deleted_by'):
        AuditLog.objects.create(
            user=instance.deleted_by,
            action='delete',
            model_name=sender.__name__,
            object_id=instance.id,
            description=f"Deleted {sender.__name__}: {instance}"
        )

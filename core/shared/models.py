"""
Base models for shared functionality.
"""

from django.db import models
from django.contrib.auth.models import User


class TimestampedModel(models.Model):
    """Abstract base model with timestamp fields."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuditModel(TimestampedModel):
    """Abstract base model with audit trail."""
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='%(class)s_created')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

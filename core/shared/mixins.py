"""
Reusable model mixins for common functionality.
"""

from django.db import models


class ActiveQuerySet(models.QuerySet):
    """QuerySet for filtering active/deleted records."""
    
    def active(self):
        return self.filter(is_deleted=False)
    
    def deleted(self):
        return self.filter(is_deleted=True)


class ActiveManager(models.Manager):
    """Manager for filtering active records by default."""
    
    def get_queryset(self):
        return ActiveQuerySet(self.model, using=self._db).active()
    
    def all_objects(self):
        return super().get_queryset()


class SoftDeleteMixin(models.Model):
    """Mixin for soft delete functionality."""
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    objects = ActiveManager()
    
    class Meta:
        abstract = True

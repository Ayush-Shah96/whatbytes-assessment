"""
Custom permission classes for Django REST Framework.
"""

from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    """Permission to check if user is a doctor."""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'doctor')


class IsPatient(permissions.BasePermission):
    """Permission to check if user is a patient."""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'patient')


class IsAdmin(permissions.BasePermission):
    """Permission to check if user is staff."""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsOwnerOrAdmin(permissions.BasePermission):
    """Permission to check if user is owner or admin."""
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user or obj.created_by == request.user

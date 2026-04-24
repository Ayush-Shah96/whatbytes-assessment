from rest_framework import permissions


class IsDoctorOrReadOnly(permissions.BasePermission):
    """Permission to allow doctors to create prescriptions."""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user, 'doctor')

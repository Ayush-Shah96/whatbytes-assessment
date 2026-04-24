from rest_framework import permissions


class IsOwnerOrDoctor(permissions.BasePermission):
    """Permission to view/edit own records or by doctor."""
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if hasattr(request.user, 'patient'):
            return obj.patient.user == request.user
        elif hasattr(request.user, 'doctor'):
            return obj.doctor.user == request.user
        return False

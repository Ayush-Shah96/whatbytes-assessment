"""Audit middleware for logging user actions."""

from .models import AuditLog
from core.shared.utils import get_client_ip


class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Log API requests
        if request.path.startswith('/api/'):
            AuditLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action='view',
                model_name=request.path,
                description=f"{request.method} {request.path}",
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
        
        return response

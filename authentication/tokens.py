"""
JWT token utilities for authentication.
"""

from rest_framework_simplejwt.tokens import Token


class CustomToken(Token):
    """Custom token with additional claims."""
    pass

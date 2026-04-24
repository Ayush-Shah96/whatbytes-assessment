"""Billing utility functions."""

from django.utils import timezone
from datetime import date
import random
import string


def generate_invoice_number():
    """Generate unique invoice number."""
    year = timezone.now().year
    prefix = f"INV-{year}-"
    random_part = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{random_part}"

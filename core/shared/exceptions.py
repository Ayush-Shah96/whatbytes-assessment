"""
Custom exception classes for the Healthcare API.
"""

from rest_framework.exceptions import APIException
from rest_framework import status


class HealthcareAPIException(APIException):
    """Base exception for Healthcare API."""
    pass


class InvalidAppointmentException(HealthcareAPIException):
    """Raised when appointment data is invalid."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid appointment data."


class DoctorNotAvailableException(HealthcareAPIException):
    """Raised when doctor is not available."""
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Doctor is not available at this time."


class PatientRecordNotFound(HealthcareAPIException):
    """Raised when patient record is not found."""
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Patient record not found."


class PrescriptionException(HealthcareAPIException):
    """Raised when prescription operation fails."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Prescription operation failed."


class BillingException(HealthcareAPIException):
    """Raised when billing operation fails."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Billing operation failed."

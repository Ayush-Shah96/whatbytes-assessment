from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer


class PatientListCreateView(APIView):
    """
    GET  /api/patients/ - List all patients created by the authenticated user.
    POST /api/patients/ - Create a new patient record.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.filter(created_by=request.user)
        serializer = PatientListSerializer(patients, many=True)
        return Response(
            {
                "success": True,
                "count": patients.count(),
                "patients": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(created_by=request.user)
        return Response(
            {
                "success": True,
                "message": "Patient created successfully.",
                "patient": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class PatientDetailView(APIView):
    """
    GET    /api/patients/<id>/ - Retrieve a specific patient.
    PUT    /api/patients/<id>/ - Update a patient record.
    DELETE /api/patients/<id>/ - Delete a patient record.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Patient, pk=pk, created_by=user)

    def get(self, request, pk):
        patient = self.get_object(pk, request.user)
        serializer = PatientSerializer(patient)
        return Response(
            {"success": True, "patient": serializer.data},
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        patient = self.get_object(pk, request.user)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Patient updated successfully.",
                "patient": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        patient = self.get_object(pk, request.user)
        patient_name = patient.name
        patient.delete()
        return Response(
            {
                "success": True,
                "message": f"Patient '{patient_name}' deleted successfully."
            },
            status=status.HTTP_200_OK
        )

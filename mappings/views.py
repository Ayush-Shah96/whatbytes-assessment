from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import PatientDoctorMapping
from .serializers import (
    PatientDoctorMappingSerializer,
    PatientDoctorMappingDetailSerializer,
    DoctorsByPatientSerializer,
)
from patients.models import Patient


class MappingListCreateView(APIView):
    """
    GET  /api/mappings/ - Retrieve all patient-doctor mappings.
    POST /api/mappings/ - Assign a doctor to a patient.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.select_related(
            'patient', 'doctor', 'assigned_by'
        ).all()
        serializer = PatientDoctorMappingDetailSerializer(mappings, many=True)
        return Response(
            {
                "success": True,
                "count": mappings.count(),
                "mappings": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        mapping = serializer.save(assigned_by=request.user)
        return Response(
            {
                "success": True,
                "message": (
                    f"Dr. {mapping.doctor.name} successfully assigned "
                    f"to patient {mapping.patient.name}."
                ),
                "mapping": PatientDoctorMappingSerializer(mapping).data
            },
            status=status.HTTP_201_CREATED
        )


class MappingsByPatientView(APIView):
    """
    GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        # Ensure the patient exists
        patient = get_object_or_404(Patient, pk=patient_id)

        mappings = PatientDoctorMapping.objects.filter(
            patient=patient
        ).select_related('doctor', 'assigned_by')

        serializer = DoctorsByPatientSerializer(mappings, many=True)
        return Response(
            {
                "success": True,
                "patient_id": patient_id,
                "patient_name": patient.name,
                "assigned_doctors_count": mappings.count(),
                "doctors": serializer.data
            },
            status=status.HTTP_200_OK
        )


class MappingDeleteView(APIView):
    """
    DELETE /api/mappings/<id>/ - Remove a doctor from a patient.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        mapping = get_object_or_404(PatientDoctorMapping, pk=pk)
        patient_name = mapping.patient.name
        doctor_name = mapping.doctor.name
        mapping.delete()
        return Response(
            {
                "success": True,
                "message": (
                    f"Dr. {doctor_name} has been removed "
                    f"from patient {patient_name}."
                )
            },
            status=status.HTTP_200_OK
        )

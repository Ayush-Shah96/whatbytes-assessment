from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Doctor
from .serializers import DoctorSerializer, DoctorListSerializer


class DoctorListCreateView(APIView):
    """
    GET  /api/doctors/ - Retrieve all doctors.
    POST /api/doctors/ - Add a new doctor (authenticated users only).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()

        # Optional filters via query params
        specialization = request.query_params.get('specialization')
        available = request.query_params.get('available')

        if specialization:
            doctors = doctors.filter(specialization=specialization)
        if available is not None:
            doctors = doctors.filter(available=available.lower() == 'true')

        serializer = DoctorListSerializer(doctors, many=True)
        return Response(
            {
                "success": True,
                "count": doctors.count(),
                "doctors": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(created_by=request.user)
        return Response(
            {
                "success": True,
                "message": "Doctor created successfully.",
                "doctor": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class DoctorDetailView(APIView):
    """
    GET    /api/doctors/<id>/ - Get details of a specific doctor.
    PUT    /api/doctors/<id>/ - Update doctor details.
    DELETE /api/doctors/<id>/ - Delete a doctor record.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Doctor, pk=pk)

    def get(self, request, pk):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(
            {"success": True, "doctor": serializer.data},
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Doctor updated successfully.",
                "doctor": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        doctor = self.get_object(pk)
        doctor_name = doctor.name
        doctor.delete()
        return Response(
            {
                "success": True,
                "message": f"Doctor '{doctor_name}' deleted successfully."
            },
            status=status.HTTP_200_OK
        )

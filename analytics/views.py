from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Count
from django.utils import timezone
from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from billing.models import Invoice


class DashboardStatsView(APIView):
    """Get dashboard statistics."""
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        today = timezone.now().date()
        
        stats = {
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'appointments_today': Appointment.objects.filter(
                appointment_time__date=today
            ).count(),
            'appointments_this_month': Appointment.objects.filter(
                appointment_time__month=today.month,
                appointment_time__year=today.year
            ).count(),
            'revenue_this_month': Invoice.objects.filter(
                created_at__month=today.month,
                created_at__year=today.year,
                status='paid'
            ).aggregate(Count('total_amount')),
        }
        return Response(stats)


class AppointmentAnalyticsView(APIView):
    """Get appointment analytics."""
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        appointments_by_status = Appointment.objects.values('status').annotate(count=Count('id'))
        return Response(list(appointments_by_status))

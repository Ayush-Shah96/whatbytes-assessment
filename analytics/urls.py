from django.urls import path
from .views import DashboardStatsView, AppointmentAnalyticsView

urlpatterns = [
    path('dashboard/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('appointments/', AppointmentAnalyticsView.as_view(), name='appointment-analytics'),
]

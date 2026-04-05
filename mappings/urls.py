from django.urls import path
from .views import MappingListCreateView, MappingsByPatientView, MappingDeleteView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:patient_id>/', MappingsByPatientView.as_view(), name='mappings-by-patient'),
    path('delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]

from patients.views import Patientlst
from django.urls import path

urlpatterns = [
    path('patients/',Patientlst, name='Patient-lst'),
]

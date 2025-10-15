from django.urls import path
from .views import find_nearby_doctors

urlpatterns = [
    path('api/doctors/nearby/', find_nearby_doctors, name='find_doctors'),
]
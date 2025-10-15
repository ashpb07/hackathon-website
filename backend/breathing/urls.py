from django.urls import path
from .views import breathing_exercise, quick_calm

urlpatterns = [
    path('breathe/', breathing_exercise),
    path('quick-calm/', quick_calm),
]
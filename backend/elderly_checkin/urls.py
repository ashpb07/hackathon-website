from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElderlyProfileViewSet, CheckInViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'elderly', ElderlyProfileViewSet)
router.register(r'checkins', CheckInViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
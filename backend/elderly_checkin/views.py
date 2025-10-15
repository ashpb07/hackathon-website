from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import ElderlyProfile, CheckIn, Reminder
from .serializers import ElderlyProfileSerializer, CheckInSerializer, ReminderSerializer
from membership.models import Member  # Import your Member model

class ElderlyProfileViewSet(viewsets.ModelViewSet):
    queryset = ElderlyProfile.objects.filter(is_active=True)
    serializer_class = ElderlyProfileSerializer

    @action(detail=False, methods=['post'])
    def register_elderly(self, request):
        member_id = request.data.get('member_id')
        # ... (same registration logic as before)

class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

    @action(detail=False, methods=['post'])
    def submit_checkin(self, request):
        member_id = request.data.get('member_id')
        # ... (same check-in logic as before)

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
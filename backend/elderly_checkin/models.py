from django.db import models
from membership.models import Member  # Import from your existing app
import uuid

class ElderlyProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    emergency_phone = models.CharField(max_length=15, blank=True, null=True)
    check_in_interval = models.IntegerField(default=6)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} (Elderly Profile)"

class CheckIn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    elderly = models.ForeignKey(ElderlyProfile, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Completed'),
        ('missed', 'Missed'),
        ('emergency', 'Emergency')
    ], default='completed')
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-check_in_time']

class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    elderly = models.ForeignKey(ElderlyProfile, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    sent = models.BooleanField(default=False)
    reminder_type = models.CharField(max_length=20, choices=[
        ('check_in', 'Check In Reminder'),
        ('follow_up', 'Follow Up Reminder'),
        ('emergency', 'Emergency Alert')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
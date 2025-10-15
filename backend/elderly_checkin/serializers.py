from rest_framework import serializers
from .models import ElderlyProfile, CheckIn, Reminder

class ElderlyProfileSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.name', read_only=True)
    member_email = serializers.CharField(source='member.email', read_only=True)
    
    class Meta:
        model = ElderlyProfile
        fields = '__all__'

class CheckInSerializer(serializers.ModelSerializer):
    elderly_name = serializers.CharField(source='elderly.member.name', read_only=True)
    
    class Meta:
        model = CheckIn
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    elderly_name = serializers.CharField(source='elderly.member.name', read_only=True)
    
    class Meta:
        model = Reminder
        fields = '__all__'
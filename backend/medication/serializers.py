from rest_framework import serializers
from .models import *

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()
    
    class Meta:
        model = Pharmacy
        fields = '__all__'
    
    def get_distance(self, obj):
        # Calculate distance from user's location
        return None  # Would be calculated in view

class MedicationPriceSerializer(serializers.ModelSerializer):
    medication_name = serializers.CharField(source='medication.name', read_only=True)
    pharmacy_name = serializers.CharField(source='pharmacy.name', read_only=True)
    price_per_unit = serializers.SerializerMethodField()
    
    class Meta:
        model = MedicationPrice
        fields = '__all__'
    
    def get_price_per_unit(self, obj):
        if obj.quantity > 0:
            return round(float(obj.price) / obj.quantity, 2)
        return 0

class PriceComparisonSerializer(serializers.Serializer):
    medication = MedicationSerializer()
    pharmacies = serializers.ListField(child=MedicationPriceSerializer())
    cheapest_option = MedicationPriceSerializer()
    average_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    savings_possible = serializers.DecimalField(max_digits=8, decimal_places=2)

class DiscountProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountProgram
        fields = '__all__'
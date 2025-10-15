from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Min, Max, Avg, Q
from django.utils import timezone
import requests
from .models import *
from .serializers import *

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    @action(detail=False, methods=['get'])
    def search_medications(self, request):
        """Search medications by name"""
        query = request.GET.get('q', '')
        if query:
            medications = Medication.objects.filter(
                Q(name__icontains=query) |
                Q(generic_name__icontains=query) |
                Q(brand_name__icontains=query)
            )[:10]
            serializer = self.get_serializer(medications, many=True)
            return Response(serializer.data)
        return Response([])

class PriceComparisonViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['post'])
    def compare_prices(self, request):
        """
        Compare medication prices across pharmacies
        POST: {
            "medication_id": "uuid",
            "user_lat": 40.7128,
            "user_lng": -74.0060,
            "radius": 10,  # miles
            "quantity": 30
        }
        """
        medication_id = request.data.get('medication_id')
        user_lat = request.data.get('user_lat')
        user_lng = request.data.get('user_lng')
        radius = request.data.get('radius', 10)
        quantity = request.data.get('quantity', 30)

        try:
            medication = Medication.objects.get(id=medication_id)
            
            # Find nearby pharmacies (simplified - would use geospatial query)
            nearby_pharmacies = self.get_nearby_pharmacies(user_lat, user_lng, radius)
            
            # Get prices for this medication
            prices = MedicationPrice.objects.filter(
                medication=medication,
                pharmacy__in=nearby_pharmacies,
                in_stock=True
            ).select_related('pharmacy')

            if not prices:
                return Response({
                    'error': 'No prices found for this medication in your area'
                }, status=404)

            # Calculate price statistics
            price_list = [float(price.price) for price in prices]
            cheapest = min(prices, key=lambda x: float(x.price))
            average_price = sum(price_list) / len(price_list)
            savings = max(price_list) - min(price_list)

            # Log the search
            UserMedicationSearch.objects.create(
                user=request.user,
                medication_name=medication.name,
                location=f"{user_lat},{user_lng}",
                results_count=len(prices)
            )

            response_data = {
                'medication': MedicationSerializer(medication).data,
                'pharmacies': MedicationPriceSerializer(prices, many=True).data,
                'cheapest_option': MedicationPriceSerializer(cheapest).data,
                'price_range': {
                    'min': min(price_list),
                    'max': max(price_list),
                    'average': round(average_price, 2)
                },
                'potential_savings': round(savings, 2),
                'pharmacies_found': len(prices)
            }

            return Response(response_data)

        except Medication.DoesNotExist:
            return Response({'error': 'Medication not found'}, status=404)

    def get_nearby_pharmacies(self, lat, lng, radius):
        """Get pharmacies within radius (simplified version)"""
        # In production, use PostGIS or geospatial queries
        return Pharmacy.objects.all()[:20]  # Mock - return first 20

    @action(detail=False, methods=['post'])
    def find_generic_alternatives(self, request):
        """Find cheaper generic alternatives"""
        brand_medication_id = request.data.get('medication_id')
        
        try:
            brand_med = Medication.objects.get(id=brand_medication_id)
            generic_meds = Medication.objects.filter(
                generic_name=brand_med.generic_name
            ).exclude(id=brand_medication_id)
            
            # Compare prices
            comparisons = []
            for generic in generic_meds:
                generic_prices = MedicationPrice.objects.filter(
                    medication=generic, 
                    in_stock=True
                )
                if generic_prices:
                    avg_generic_price = generic_prices.aggregate(Avg('price'))['price__avg']
                    brand_prices = MedicationPrice.objects.filter(medication=brand_med)
                    avg_brand_price = brand_prices.aggregate(Avg('price'))['price__avg'] if brand_prices else 0
                    
                    savings = float(avg_brand_price) - float(avg_generic_price) if avg_brand_price else 0
                    
                    comparisons.append({
                        'generic_medication': MedicationSerializer(generic).data,
                        'average_price': avg_generic_price,
                        'potential_savings': round(savings, 2),
                        'savings_percentage': round((savings / float(avg_brand_price)) * 100, 2) if avg_brand_price else 0
                    })
            
            return Response(sorted(comparisons, key=lambda x: x['average_price']))
            
        except Medication.DoesNotExist:
            return Response({'error': 'Medication not found'}, status=404)

class DiscountProgramViewSet(viewsets.ModelViewSet):
    queryset = DiscountProgram.objects.filter(
        Q(valid_until__isnull=True) | Q(valid_until__gte=timezone.now())
    )
    serializer_class = DiscountProgramSerializer

    @action(detail=False, methods=['post'])
    def check_eligibility(self, request):
        """Check user eligibility for discount programs"""
        user_data = request.data
        programs = self.get_queryset()
        
        eligible_programs = []
        for program in programs:
            # Check eligibility based on user data (age, income, insurance, etc.)
            if self.is_eligible(program, user_data):
                eligible_programs.append(program)
        
        serializer = self.get_serializer(eligible_programs, many=True)
        return Response(serializer.data)

    def is_eligible(self, program, user_data):
        """Check if user meets program criteria"""
        # Implement eligibility logic based on program criteria
        # This would check age, income, insurance status, etc.
        return True  # Simplified

class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

    @action(detail=True, methods=['get'])
    def inventory(self, request, pk=None):
        """Get all medications available at a pharmacy"""
        pharmacy = self.get_object()
        prices = MedicationPrice.objects.filter(
            pharmacy=pharmacy, 
            in_stock=True
        ).select_related('medication')
        serializer = MedicationPriceSerializer(prices, many=True)
        return Response(serializer.data)
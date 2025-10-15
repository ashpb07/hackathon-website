import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def find_nearby_doctors(request):
    """
    Find nearby doctors - no database storage
    POST: {"disease": "heart", "lat": 40.7128, "lng": -74.0060, "radius": 5000}
    """
    try:
        disease = request.data.get('disease', '').lower()
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        radius = request.data.get('radius', 5000)

        if not lat or not lng:
            return Response({'error': 'Latitude and longitude required'}, status=400)

        # Disease to specialty mapping
        specialty_map = {
            'heart': 'cardiologist', 'chest': 'cardiologist', 'blood pressure': 'cardiologist',
            'diabetes': 'endocrinologist', 'sugar': 'endocrinologist',
            'arthritis': 'rheumatologist', 'joint': 'rheumatologist',
            'asthma': 'pulmonologist', 'breathing': 'pulmonologist', 'lung': 'pulmonologist',
            'cancer': 'oncologist', 'oncology': 'oncologist',
            'brain': 'neurologist', 'headache': 'neurologist', 'stroke': 'neurologist',
            'mental': 'psychiatrist', 'depression': 'psychiatrist', 'anxiety': 'psychiatrist',
            'skin': 'dermatologist', 'rash': 'dermatologist',
            'eye': 'ophthalmologist', 'vision': 'ophthalmologist',
            'ear': 'ent', 'nose': 'ent', 'throat': 'ent',
            'stomach': 'gastroenterologist', 'digestion': 'gastroenterologist',
            'kidney': 'nephrologist', 'bone': 'orthopedic', 'fracture': 'orthopedic'
        }

        specialty = 'doctor'
        for keyword, spec in specialty_map.items():
            if keyword in disease:
                specialty = spec
                break

        # Google Places API call
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            'key': settings.GOOGLE_MAPS_API_KEY,
            'location': f"{lat},{lng}",
            'radius': radius,
            'keyword': f'{specialty} hospital clinic',
            'type': 'doctor'
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] != 'OK':
            return Response({'error': f"Google API error: {data['status']}"}, status=400)

        # Process results
        doctors = []
        for place in data['results'][:15]:
            doctor = {
                'name': place.get('name'),
                'address': place.get('vicinity'),
                'rating': place.get('rating'),
                'total_ratings': place.get('user_ratings_total', 0),
                'place_id': place.get('place_id'),
                'specialty': specialty,
                'location': place.get('geometry', {}).get('location', {})
            }
            doctors.append(doctor)

        return Response({
            'specialty': specialty,
            'disease': disease,
            'doctors_found': len(doctors),
            'doctors': doctors
        })

    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def get_google_maps_key(request):
    """
    Return Google Maps API key for frontend
    (Be careful with this - only use if you have domain restrictions)
    """
    return Response({
        'maps_key': settings.GOOGLE_MAPS_API_KEY
    })
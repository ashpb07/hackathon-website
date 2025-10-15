from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

@api_view(['GET'])
def breathing_exercise(request):
    """
    Ultra-simple breathing exercise - no data storage
    """
    techniques = [
        {
            'name': '4-7-8 Breathing',
            'inhale': 4,
            'hold': 7, 
            'exhale': 8,
            'cycles': 4,
            'description': 'Calming technique for stress relief'
        },
        {
            'name': 'Box Breathing',
            'inhale': 4,
            'hold': 4,
            'exhale': 4,
            'cycles': 5,
            'description': 'Navy SEAL technique for focus'
        },
        {
            'name': 'Deep Breathing', 
            'inhale': 5,
            'hold': 0,
            'exhale': 5,
            'cycles': 6,
            'description': 'Simple relaxation breathing'
        }
    ]
    
    # Return random technique each time
    technique = random.choice(techniques)
    
    return Response(technique)

@api_view(['GET']) 
def quick_calm(request):
    """
    Even simpler - one button instant calm
    """
    return Response({
        'instruction': 'Breathe slowly for 1 minute',
        'animation': 'circle_pulse',
        'duration': 60
    })
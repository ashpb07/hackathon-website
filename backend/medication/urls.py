from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'medications', MedicationViewSet)
router.register(r'pharmacies', PharmacyViewSet)
router.register(r'discount-programs', DiscountProgramViewSet)
router.register(r'price-comparison', PriceComparisonViewSet, basename='price-comparison')

urlpatterns = [
    path('api/', include(router.urls)),
]
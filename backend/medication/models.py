from django.db import models
import uuid

class Medication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)
    strength = models.CharField(max_length=50)
    form = models.CharField(max_length=50)  # tablet, capsule, liquid, etc.
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Pharmacy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    chain_name = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=20, blank=True)
    hours = models.JSONField(default=dict)  # Store opening hours as JSON

class MedicationPrice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()  # Number of pills/bottles
    last_updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)

class UserMedicationSearch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)
    results_count = models.IntegerField(default=0)

class DiscountProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    eligibility_criteria = models.TextField(blank=True)
    valid_until = models.DateField(null=True, blank=True)
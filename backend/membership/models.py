from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField( max_length=50)
    username=models.CharField(max_length=20)
    email=models.EmailField( max_length=254)
    pass1=models.CharField( max_length=20)
    pass2=models.CharField(max_length=20)
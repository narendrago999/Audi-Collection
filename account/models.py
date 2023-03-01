from django.db import models

# Create your models here.
class account(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField (max_length=254)
    number = models.IntegerField()
    state = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    password = models.CharField(max_length=50)
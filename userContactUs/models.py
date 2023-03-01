from django.db import models

# Create your models here.
class userContacted(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField (max_length=254)
    question = models.TextField()
    
from django.db import models

# Create your models here.
class product_info(models.Model):
    product_image = models.ImageField(upload_to="productImages", height_field=None, width_field=None, max_length=None)
    product_title= models.CharField(max_length=50, default="mobile")
    product_price = models.IntegerField()
    product_desc = models.TextField()
    product_rating = models.IntegerField()



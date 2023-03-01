from django.contrib import admin
from product.models import product_info

class mkadmin(admin.ModelAdmin):
    list_display = ["product_image", "product_price", "product_desc", "product_rating"]
admin.site.register(product_info, mkadmin)    
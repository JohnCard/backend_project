from django.contrib import admin

# Register your models here.
from .models import Product,DigitalProduct

admin.site.register(Product)
admin.site.register(DigitalProduct)
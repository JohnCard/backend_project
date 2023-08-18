
from django.contrib import admin
from .models import User, Market,Product, ProductSec

# Register your models here.
admin.site.register(User)
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(ProductSec)

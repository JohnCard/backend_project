from colorfield.fields import ColorField
from django.db import models 
# Create your models here.

class Product(models.Model):
    title = models.TextField(max_length=100, default='Prducto nuevo')# title product
    price = models.FloatField(default=100) # price product
    description = models.CharField(max_length=100,default='On sale') # description product
    color = ColorField(null = True) # color product
    slug = models.SlugField(db_index=True, blank = True,default='new-product') # slug product
    def __str__(self): # main function
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=200) # username
    credit_card = models.JSONField() # credit cart
    telephone = models.IntegerField() # phone user
    email = models.EmailField() # email
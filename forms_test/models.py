from django.db import models
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) # title product
    slug = models.SlugField(unique=True) # slug product
    price = models.FloatField() # price product

class User(models.Model):
    name = models.CharField(max_length=50) # username
    second_name = models.CharField(max_length=50) # second name
    email = models.EmailField() # email
    password = models.CharField(max_length=50) # pasword
    password_confirmation = models.CharField(max_length=50) # password confirmation

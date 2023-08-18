from django.db import models
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    price = models.FloatField()

class User(models.Model):
    name = models.CharField(max_length=50)
    sec_nm = models.CharField(max_length=50)
    gm = models.EmailField()
    psw = models.CharField(max_length=50)
    ps_conf = models.CharField(max_length=50)

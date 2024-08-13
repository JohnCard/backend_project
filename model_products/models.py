from django.db import models
from django.conf import settings
from colorfield.fields import ColorField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # user foreign key
    title = models.CharField(max_length=60) # title product
    slug = models.SlugField(unique=True) # slug product
    color = ColorField(default='#FF0000') # color product
    created = models.DateTimeField(auto_now_add=True) # created date
    price = models.IntegerField(default=450) # price product
    
    def __str__(self): # main function
        return self.title
    
    def get_absolute_url(self): # go to detail instance page
        return f'/detail/{self.slug}'
    
    def get_edit_url(self): # go to update page
        return f'/update/{self.slug}'
    
    def get_delete_url(self):
        return f'/update/{self.slug}/delete/' # go to delete page

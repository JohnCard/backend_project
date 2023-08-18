from django.db import models
from django.conf import settings
from colorfield.fields import ColorField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    color = ColorField(default='#FF0000')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/detail/{self.slug}'
    
    def get_edit_url(self):
        return f'/update/{self.slug}'
    
    def get_delete_url(self):
        return f'/update/{self.slug}/delete/'
    
    
class DigitalProduct(Product):
    class Meta:
        proxy = True
        

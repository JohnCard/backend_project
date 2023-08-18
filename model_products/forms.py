#comment
from django import forms 
from .models import DigitalProduct, Product

class SecModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'color'
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'color'
        ]

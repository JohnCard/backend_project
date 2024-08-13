#comment
from django import forms 
from .models import Product

class SecondModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'color',
            'price'
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'color',
            'price'
        ]

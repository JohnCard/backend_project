# 1st comment
from django import forms
# from django.forms.widgets import TextInput
from .models import User,Product

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'credit_card',
            'tel',
            'gmail',
            'shoping_cart',
            'id_market'
        ]
        
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
            'color',
            'seller',
            'product_dimensions'
        ]
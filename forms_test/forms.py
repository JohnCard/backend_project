#comment
from django import forms 
from .models import Product, User
from .functions import validate

MY_CHOICES = [
    ('DB-VAL1', 'OPT1'),
    ('DB-VAL2', 'OPT2'),
    ('DB-VAL3', 'OPT3')
]

YEARS = [x for x in range(1900,2023)]

class SearchForm(forms.Form):
    q = forms.CharField()
    
class TestForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS)) # date field
    text = forms.CharField() # text field
    bool = forms.BooleanField() # bool field
    integer = forms.IntegerField() # integer num field
    email = forms.EmailField() # email field
    options = forms.CharField(label='Select an option', widget=forms.Select(choices=MY_CHOICES)) # select field
    # radio field
    opciones_radio = forms.CharField(label='Select an option', widget=forms.RadioSelect(choices=MY_CHOICES)) 
    # checkbox field
    opciones_checkbox = forms.CharField(label='Select an option', widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))
    
    def clean_integer(self, *args, **kwargs):
        # pull int data
        int_field = self.cleaned_data.get("integer")
        # ? bigger than 100?
        if int_field > 100:
            raise forms.ValidationError('El número debe ser menor o igual que 100')
        return int_field
    
    def clean_text(self, *args, **kwargs):
        # validate text field
        text = self.cleaned_data.get("text")
        # ? smaller than 10?
        if len(text) < 10:
            raise forms.ValidationError('El texto debe contener más alla de 10 letras o carácteres')
        return text
    
class UserModel(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'second_name',
            'email',
            'password',
            'password_confirmation',
        ]
        
    def clean_name(self, *args, **kwargs):
        # get name parameter
        name = self.cleaned_data.get('name')
        # ? bigger than?
        if validate(name) > 0:
            # ! bad request
            raise forms.ValidationError('Este campo no es válido como nombre!!!')
        return name
    
    def clean_second_name(self, *args, **kwargs):
        # second name
        second_name = self.cleaned_data.get('second_name')
        # ? length bigger than 0?
        if validate(second_name) > 0:
            # ! bad request
            raise forms.ValidationError('Este campo no es válido como apellido!!!')
        return second_name
    
    def clean_password(self, *args, **kwargs):
        # get password parameter
        password = self.cleaned_data.get('password')
        # ? length smaller/bigger than 10/18?
        if len(password) < 10 and len(password) > 18:
            # ! bad request
            raise forms.ValidationError('En su contraseña debe crequerir más alla de 10 letras o carácteres!!!')
        return password
    
    def clean_password_confirmation(self, *args, **kwargs):
        # confirmation
        confirmation = self.cleaned_data.get('password_confirmation')
        password = self.cleaned_data.get('password')
        # ? get confirmation parameter
        if confirmation != password:
            # ! bad request
            raise forms.ValidationError('Este campo es diferente de la contraseña original!!!')
        return confirmation
    
class ProductModel(forms.ModelForm):
    class Meta:
        labels = {
        'title': 'My title label',
        'slug': 'Slug label',
        'price': 'Price label'    
        }
        
        model = Product
        fields = [
            'title',
            'slug',
            'price'
        ]
        exclude = []
    
    def clean_title(self, *args, **kwargs):
        # get title parameter
        one_text = self.cleaned_data.get('title')
        # ? length smaller/equal 10?
        if len(one_text) <= 10:
            # ! bad request
            raise forms.ValidationError('El texto debe contener más alla de 10 letras o carácteres')
        return one_text
    
    def clean_slug(self, *args, **kwargs):
        # get slug
        slug = self.cleaned_data.get('slug')
        # ? length smaller/equal 10?
        if len(slug) <= 10:
            # ! bad request
            raise forms.ValidationError('Nuestro slug debe contener más alla de 10 letritas o carácteres')
        if 'misupermarca' not in slug:
            # ! bad request
            raise forms.ValidationError('Nuestro slug debe incluir o contener misupermarca')
        return slug
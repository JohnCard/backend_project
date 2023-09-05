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
    fecha = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    un_texto = forms.CharField()
    bool_field = forms.BooleanField()
    int_field = forms.IntegerField()
    corr = forms.EmailField()
    opciones = forms.CharField(label='Select an option', widget=forms.Select(choices=MY_CHOICES))
    opciones_radio = forms.CharField(label='Select an option', widget=forms.RadioSelect(choices=MY_CHOICES))
    opciones_checkbox = forms.CharField(label='Select an option', widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))
    
    def clean_int_field(self, *args, **kwargs):
        int_field = self.cleaned_data.get("int_field")
        if int_field > 100:
            raise forms.ValidationError('El número debe ser menor o igual que 100')
        return int_field
    
    def clean_un_texto(self, *args, **kwargs):
        one_text = self.cleaned_data.get("un_texto")
        if len(one_text) < 10:
            raise forms.ValidationError('El texto debe contener más alla de 10 letras o carácteres')
        return one_text
    
class UserModel(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'sec_nm',
            'gm',
            'psw',
            'ps_conf'
        ]
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if validate(name) > 0:
            raise forms.ValidationError('Este campo no es válido como nombre!!!')
        return name
    
    def clean_sec_nm(self, *args, **kwargs):
        sec_nm = self.cleaned_data.get('sec_nm')
        if validate(sec_nm) > 0: 
            raise forms.ValidationError('Este campo no es válido como apellido!!!')
        return sec_nm
    
    def clean_psw(self, *args, **kwargs):
        pswd = self.cleaned_data.get('psw')
        if len(pswd) < 10 and len(pswd) > 18:
            raise forms.ValidationError('En su contraseña debe crequerir más alla de 10 letras o carácteres!!!')
        return pswd
    
    def clean_ps_conf(self, *args, **kwargs):
        conf = self.cleaned_data.get('ps_conf')
        if conf != self.cleaned_data.get('psw'):
            raise forms.ValidationError('Este campo es diferente de la contraseña original!!!')
        return conf
    
class ProductModel(forms.ModelForm):
    
    class Meta:
        labels = {
        'title':'My title label',
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
        one_text = self.cleaned_data.get('title')
        if len(one_text) <= 10:
            raise forms.ValidationError('El texto debe contener más alla de 10 letras o carácteres')
        return one_text
    
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug')
        if len(slug) <= 10:
            raise forms.ValidationError('nuestro slug debe contener más alla de 10 letritas o carácteres')
        if 'misupermarca' not in slug:
            raise forms.ValidationError('Nuestro slug debe incluir o contener misupermarca')
        return slug
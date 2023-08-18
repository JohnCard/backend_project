from django.shortcuts import render
from .forms import SearchForm, TestForm, ProductModel, UserModel
from django.forms import formset_factory, modelformset_factory
from .models import Product,User
# Create your views here.

def seach_form(request):
    ###### 1er 
    form = SearchForm()
    ###### 2er 
    form_product = ProductModel(request.POST or None)
    ###### 3er 
    initial_data = {
        'texto': 'texto inicial',
        'booleano': True,
        'entero': 100,
        'correo': 'test@test.com'
    }
    form_test = TestForm(request.POST or None, initial=initial_data)
    ###### 4er 
    test_form = formset_factory(TestForm, extra=3)
    formset = test_form(request.POST or None)
    ###### 5er
    ProductFormSet = modelformset_factory(Product, form=ProductModel)
    formset_two = ProductFormSet(request.POST or None, queryset=Product.objects.all())
    
    print('formset.data')
    print(formset.data)
    
    print('formset.errors')
    print(formset.errors)
    
    ################################
    values = {
        'form': form,
        'form_test': form_test,
        'form_product': form_product,
        'test_form': formset,
        'context': formset_two
    }
    return render(request, 'pages/form_sec.html', values)

def homework_form(request):
    form = UserModel(request.POST or None)
    if form.is_valid():
        form.save()
    values = {
        'form': form,
    }
    return render(request, 'pages/form_homw.html', values)
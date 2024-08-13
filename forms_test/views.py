from django.shortcuts import render
from .forms import SearchForm, TestForm, ProductModel, UserModel
from django.forms import formset_factory, modelformset_factory
from .models import Product,User
# Create your views here.

def seach_form(request):
    # search form
    form = SearchForm()
    # second form 
    form_product = ProductModel(request.POST or None)
    # third form
    initial_data = {
        'un_texto': 'texto inicial',
        'bool_field': True,
        'int_field': 100,
        'corr': 'test@test.com'
    }
    form_test = TestForm(request.POST or None, initial=initial_data)
    # fourth form
    test_form = formset_factory(TestForm, extra=3)
    form_set = test_form(request.POST or None)
    # fifth form
    product_form_set = modelformset_factory(Product, form=ProductModel)
    formset_two = product_form_set(request.POST or None, queryset=Product.objects.all())
    # form values
    values = {
        'form': form,
        'form_test': form_test,
        'form_product': form_product,
        'test_form': form_set,
        'context': formset_two
    }
    return render(request, 'pages/form_sec.html', values)

def homework_form(request):
    # user model
    form = UserModel(request.POST or None)
    # ? valid data?
    if form.is_valid():
        # * save data
        form.save()
    values = {
        'form': form,
    }
    return render(request, 'pages/form_homw.html', values)
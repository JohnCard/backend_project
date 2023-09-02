from django.shortcuts import render, get_object_or_404
from .models import User, returning_message_markets, Market,Product,ProductSec
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductModelForm
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def update_view(request, product_id=None):
    instance = get_object_or_404(Product, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Producto actualizado con éxito!!!')
        return HttpResponseRedirect(f'/detail_view/{instance.id}')
    context = {
        'form': form,
        'product': instance
    }
    return render(request, 'pages/update_view.html', context)

def delete_view(request, product_id):
    instance = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request,'Producto eliminado con éxito!!!')
        return HttpResponseRedirect('/list_view')
    context = {
        'product': instance
    }
    
    return render(request, 'pages/delete_view.html',context)

def detail_view(request,product_id):
    instance = get_object_or_404(Product,id=product_id)
    context = {
        'product': instance
    } 
    return render(request, 'pages/detail_view.html',context)

def list_view(request):
    query = request.GET.get('q',None)
    queryset = Product.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query) |
            Q(color__icontains=query) |
            Q(product_dimensions__icontains=query)
        )
    var = {'product_list':queryset}
    if request.user.is_authenticated:
        return render(request,'pages/list_view.html',var)
    else:
        return render(request, 'pages/public.html')

def creating_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Producto creado con éxito')
        return HttpResponseRedirect(f'/detail_view/{instance.id}')
    context = {
        'form': form
    }
    return render(request, 'pages/creating_view.html',context)

def first_user(request):
    var = User.objects.get(id=1)
    return render(request, 'pages/first_user.html',{'var': var})

def test(request):
    product_list = []
    product_list.extend(Market.objects.get(id=1).articles.keys())
    product_list.extend(Market.objects.get(id=2).articles.keys())
    product_list.extend(Market.objects.get(id=3).articles.keys())
    dicct = {
        'var':returning_message_markets('1',1),
        'var_sec': product_list,
        'cont': 0,
        'cont_sec': 1
    }
    return render(request, 'pages/test.html', dicct)

# def home(request):
#     response = HttpResponse()
#     response.write('<p>Texto de prueba</p>')
#     response.write('<p>Texto de prueba</p>')
#     response.write('<p>Texto de prueba</p>')
#     return response

# def home(request):
#     response = HttpResponse()
#     response.write('<p>Texto de prueba</p>')
#     response.write('<p>Texto de prueba</p>')
#     response.write('<p>Texto de prueba</p>')
#     response.content = '<h1>Voy hijo de tu $%&#$%$#& madre!!!</h1>'
#     response.write('<p>Texto de prueba</p>')
#     return response

def home(request):
    response = HttpResponse()
    response.write('<p>Texto de prueba</p>')
    response.status_code = 400
    return response

def redirection_two(request):
    return HttpResponseRedirect('/home')

def product_models(request):
    return HttpResponse('Un ecommerce personalizado')

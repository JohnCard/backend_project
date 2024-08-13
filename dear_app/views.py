from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Product
from .forms import ProductModelForm

# Create your views here.

def update_view(request, product_id=None):
    # get instance or 404 error
    instance = get_object_or_404(Product, id=product_id)
    # filter form by instance
    form = ProductModelForm(request.POST or None, instance=instance)
    # ? valid data?
    if form.is_valid():
        #* save data
        instance = form.save(commit=False)
        instance.save()
        # throw succes message
        messages.success(request,'Producto actualizado con éxito!!!')
        return HttpResponseRedirect(f'/detail-view/{instance.id}')
    context = {
        'form': form,
        'product': instance
    }
    return render(request, 'pages/update_view.html', context)

def delete_view(request, product_id):
    # get instance or 404 error
    instance = get_object_or_404(Product, id=product_id)
    # ? post method?
    if request.method == 'POST':
        # delete instance
        instance.delete()
        # throw succes message
        messages.success(request,'Producto eliminado con éxito!!!')
        return HttpResponseRedirect('/list-view')
    context = {
        'product': instance
    }
    return render(request, 'pages/delete_view.html',context)

def detail_view(request,product_id):
    # get instance or 404 error
    instance = get_object_or_404(Product, id=product_id)
    context = {
        'product': instance
    } 
    return render(request, 'pages/detail_view.html',context)

def list_view(request):
    # get query param
    query = request.GET.get('q',None)
    # define queryset
    queryset = Product.objects.all()
    # ? valid query?
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query) |
            Q(color__icontains=query) 
        )
    context = {'product_list':queryset}
    # ? authenticated user?
    if request.user.is_authenticated:
        return render(request,'pages/list_view.html', context)
    # ! not authenticated
    else:
        return render(request, 'pages/public.html')

def creating_view(request):
    # get instance form
    form = ProductModelForm(request.POST or None)
    # ? valid data?
    if form.is_valid():
        # save new instance
        instance = form.save(commit=False)
        instance.save()
        # throw succes message
        messages.success(request, 'Producto creado con éxito')
        return HttpResponseRedirect(f'/detail-view/{instance.id}')
    context = {
        'form': form
    }
    return render(request, 'pages/creating_view.html',context)
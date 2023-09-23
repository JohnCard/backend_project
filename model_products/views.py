from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
from rest_framework import generics, viewsets
from .pagination import ProductPagination, ProductLOPag, ProductCPag
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
##########
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.conf import settings
# User = settings.AUTH_USER_MODEL
session_key = 'pauzhhgqhy7cyw82g85ksrfdr6jxqcxa'
session = Session.objects.get(session_key=session_key)
session_data = session.get_decoded()
uid = session_data.get('_auth_user_id')
# user = User.objects.get(id=uid)
# print(User.objects.all())
# print(f'Second {User.objects.filter(id=1)}')
# print(f'Third One {User.objects.get(id=1).last_login}')

# Create your views here.
from .mixins import TemplateTitleMixin,TemplateTitleMixinSc
from .models import Product
from .forms import ProductForm, SecModelForm

class ProductList(generics.ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductCPag
    permission_classes = [
        IsAuthenticated
    ]
    
class ProductForm(CreateView,TemplateTitleMixinSc,ListView):
    form_class = ProductForm
    template_name = 'pages/forms.html'
    link_cancel = '/my-products/'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(f'/my-products/')
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class ProtectedListView(LoginRequiredMixin,TemplateTitleMixin,ListView):
    model = Product
    title = 'Productos fisicos'
    template_name = 'pages/products.html'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
class UpdateProduct(UpdateView):
    form_class = SecModelForm
    template_name = 'pages/detail.html'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        self.object.get_edit_url()
        return '/my-products/'
        
    
class DetailProduct(DetailView):
    model = Product
    template_name = 'pages/detail.html'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)   
    
class DeleteProduct(DeleteView):
    template_name = 'pages/delete.html'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return '/my-products/'
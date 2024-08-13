from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .pagination import ProductLimitOffPagination
from .serializers import ProductSerializer
from .mixins import TemplateTitleMixin,TemplateCancel,LinkStyle
from .models import Product
from .forms import ProductForm, SecondModelForm
# Create your views here.

class ProductList(generics.ListAPIView):
    # define queryset
    queryset = Product.objects.all()
    # define serializer class
    serializer_class = ProductSerializer
    # define pagination class
    pagination_class = ProductLimitOffPagination
    # define authentication class
    permission_classes = [
        IsAuthenticated
    ]
    
class ProductForm(CreateView, TemplateCancel, LinkStyle, ListView):
    # define form class
    form_class = ProductForm
    # define template
    template_name = 'pages/forms.html'
    # define link class
    link_cancel = '/my-products/'
    # define a stylesheet
    linkstyle = 'model_products/forms.css'
    
    # define your queryset
    def get_queryset(self):
        product = Product.objects.filter(user=self.request.user)
        return product
    
    def form_valid(self,form):
        # define instance user
        form.instance.user = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect('/my-products/')
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class ProtectedListView(LoginRequiredMixin,TemplateTitleMixin,ListView):
    # define model product
    model = Product
    # define title template
    title = 'Products'
    # define template
    template_name = 'pages/products.html'
    
    def get_queryset(self):
        product = Product.objects.filter(user=self.request.user)
        return product
    
class UpdateProduct(UpdateView):
    # define form class
    form_class = SecondModelForm
    # define template
    template_name = 'pages/detail.html'
    
    def get_queryset(self):
        product = Product.objects.filter(user=self.request.user)
        return product
    
    def get_success_url(self):
        self.object.get_edit_url()
        return '/my-products/'
        
class DetailProduct(DetailView):
    # define model
    model = Product
    # define template
    template_name = 'pages/detail.html'
    
    def get_queryset(self):
        product = Product.objects.filter(user=self.request.user)
        return product
    
class DeleteProduct(DeleteView):
    # define model
    model = Product
    # define template
    template_name = 'pages/delete.html'
    
    def get_queryset(self):
        product = Product.objects.filter(user=self.request.user)
        return product
    
    def get_success_url(self):
        return '/my-products/'
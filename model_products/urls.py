# comment
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from rest_framework.routers import DefaultRouter
from .views import ProtectedListView, ProductForm,UpdateProduct, DeleteProduct, DetailProduct,ProductList

urlpatterns = [
    path('creating_products/',ProductForm.as_view()),
    path('my-products/',ProtectedListView.as_view()),
    path('update/<slug:slug>/',UpdateProduct.as_view()),
    path('update/<slug:slug>/delete/',DeleteProduct.as_view()),
    path('detail/<slug:slug>/',DetailProduct.as_view()),
    path('ProductView/',ProductList.as_view()),
]

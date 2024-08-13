# comment
from django.urls import path
from .views import ProtectedListView, ProductForm, UpdateProduct, DeleteProduct, DetailProduct, ProductList

urlpatterns = [
    # create a new product
    path('creating-products/', ProductForm.as_view()),
    # list products
    path('my-products/', ProtectedListView.as_view()),
    # update a product
    path('update/<slug:slug>/', UpdateProduct.as_view()),
    # delete a product
    path('update/<slug:slug>/delete/', DeleteProduct.as_view()),
    # retrieve a product
    path('detail/<slug:slug>/', DetailProduct.as_view()),
    # list product
    path('product-view/', ProductList.as_view()),
]
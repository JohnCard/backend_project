from django.urls import path
from .views import index, first_user,creating_view,test,home,redirection_two,product_models,detail_view,list_view, update_view, delete_view

urlpatterns = [
    path('index/', index,name='index'),
    path('detail_view/<int:product_id>',detail_view,name='detail_view'),
    path('list_view/',list_view,name='list_view'),
    path('creating_view/', creating_view, name='creating_view'),
    path('update_view/<int:product_id>', update_view, name='update_view'),
    path('delete_view/<int:product_id>', delete_view, name='delete_view'),
    path('first_user/',first_user,name='first_user'),
    path('test/', test, name='test'),
    path('home/', home, name='home'),
    path('redirection_two/', redirection_two, name='redirection_two'),
    path('product_models/', product_models, name='product_models')
]

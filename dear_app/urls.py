from django.urls import path
from .views import creating_view, detail_view, list_view, update_view, delete_view

urlpatterns = [
    path('detail-view/<int:product_id>', detail_view, name='detail_view'), # detail instance page
    path('list-view/', list_view, name='list_view'), # list instances page
    path('creating-view/', creating_view, name='creating_view'), # create instance
    path('update-view/<int:product_id>', update_view, name='update_view'), # update an instance
    path('delete-view/<int:product_id>', delete_view, name='delete_view'), # delete an instance
]

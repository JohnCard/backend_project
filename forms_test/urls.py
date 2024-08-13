from django.urls import path
from .views import seach_form, homework_form

urlpatterns = [
    # search form
    path('search-form/', seach_form),
    # form homework
    path('form-homework/', homework_form),
]
#comment
from django.urls import path

from .views import seach_form, homework_form

urlpatterns = [
    path('seach_form/',seach_form),
    path('form_homw/',homework_form)
]
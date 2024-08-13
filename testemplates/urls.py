from django.urls import path
from .views import test_view, second_test, detail_object, test

urlpatterns = [
    path('test-view/', test_view), # first test view
    path('second-test/', second_test), # second test view
    path('detail-object/', detail_object), # detail object
    path('testings/', test) # final testings
]
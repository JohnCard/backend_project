from django.urls import path,include
from .views import TestAPIView,SecView
from rest_framework.routers import DefaultRouter
from .serializers import Programmer

router = DefaultRouter()
router.register('api_third',SecView,basename='api_third')
# router.register('api_fourth',TestAPIView,basename='api_fourth')

urlpatterns = [
    path('api_sec/',TestAPIView.as_view()),
    path('',include(router.urls))
]

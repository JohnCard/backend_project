from rest_framework import routers
from .api import ProjectView, ProjectViewSCND,ProjectViewSC
from django.urls import path,include
from .views import ProductAPIView

router = routers.DefaultRouter()

router.register('api/projects', ProjectView,'Projects')
router.register('api/projectscnd', ProjectViewSCND,'ProjectSCND')
# router.register('api/second_api', ProjectViewSC,'ProjectSC')

urlpatterns = [
    path('first_api/',ProductAPIView.as_view()),
    path('sec_api_view/',ProjectViewSC.as_view()),
    
    path('',include(router.urls))
]
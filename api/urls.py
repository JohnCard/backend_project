from rest_framework import routers
from .api import ProjectView, ProjectViewSCND,ProjectViewSC,fourth_project
from django.urls import path,include
from .views import ProductAPIView, ProjectThrd

router = routers.DefaultRouter()

router.register('api/projects', ProjectView,'Projects')
router.register('api/projectscnd', ProjectViewSCND,'ProjectSCND')

urlpatterns = [
    path('first_api/',ProductAPIView.as_view()),
    path('sec_api_view/<int:id>',ProjectViewSC.as_view()),
    path('third_api/',ProjectThrd.as_view()),
    path('fourth_item/<int:pk>',fourth_project,name='fourth_project'),
    path('',include(router.urls))
]
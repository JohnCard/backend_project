from django.urls import path
from .views import FirstProjectAPIView, SecondProjectAPIView

urlpatterns = [
    # first api project
    path('first-api-project/<int:id>', FirstProjectAPIView.as_view()),
    # third api project
    path('third-api-project/<int:id>', SecondProjectAPIView.as_view())
]
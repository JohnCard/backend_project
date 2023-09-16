from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view_tk, logout_view, registration_view_JW, profile_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view_tk,name='register'),
    path('logout/',logout_view,name='logout'),
    path('profile_view/',profile_view,name='profile view'),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view())
]
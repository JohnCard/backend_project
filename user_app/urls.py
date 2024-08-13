from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view_tk, logout_view, profile_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # login
    path('login/', obtain_auth_token, name='login'),
    # register
    path('register/', registration_view_tk, name='register'),
    # logout
    path('logout/', logout_view, name='logout'),
    # profile view
    path('profile-view/', profile_view, name='profile view'),
    # get token
    path('api/token/', TokenObtainPairView.as_view()),
    # refresh token
    path('api/token/refresh/', TokenRefreshView.as_view())
]
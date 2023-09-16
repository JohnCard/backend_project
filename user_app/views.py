from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
#####
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here.

@api_view(['POST'])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view_tk(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Registro exitoso!!!'
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else:
            return Response(serializer.errors)    
        
        return Response(data)
    
@api_view(['GET'])
def profile_view(request):
    # MY USER KEY CHOICES:
    '''
    auth_token, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, product, project, user_permissions, username
    '''
    # user = User.objects.get(id=request.data['id'])
    user = request.user
    print(user.is_authenticated)
    if user.is_authenticated:
        user_response = {
            'User name': user.username,
            'email': user.email,
            'id': user.pk
        }
    else:
        user_response = {}
    return Response(user_response)
    
        
@api_view(['POST',])
def registration_view_JW(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Registro exitoso!!!'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh_token = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token)
            }
        else:
            return Response(serializer.errors)    
        
        return Response(data)


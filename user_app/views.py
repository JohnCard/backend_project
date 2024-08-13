from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(['POST'])
def logout_view(request):
    # ? post method?
    if request.method == 'POST':
        # delete token
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view_tk(request):
    # ? post method?
    if request.method == 'POST':
        # define register serializer
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        # ? valid data?
        if serializer.is_valid():
            # * save data
            account = serializer.save()
            # prepare main response
            data['response'] = 'Registro exitoso!!!'
            data['username'] = account.username
            data['email'] = account.email
            # get current token
            token = Token.objects.get(user=account).key
            data['token'] = token
        # ! bad request
        else:
            return Response(serializer.errors)    
        return Response(data)
    
@api_view(['GET'])
def profile_view(request):
    '''
    MY USER KEY CHOICES:
    auth_token, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, product, project, user_permissions, username
    '''
    # get user
    user = request.user
    # ? authenticated?
    if user.is_authenticated:
        # * prepare main response
        user_response = {
            'User name': user.username,
            'email': user.email,
            'id': user.pk
        }
    # ! bad request
    else:
        user_response = {'Message': 'It didn´t works'}
    return Response(user_response)  
        
@api_view(['POST',])
def registration_view_JW(request):
    # ? post method?
    if request.method == 'POST':
        # define serializer
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        # ? valid data?
        if serializer.is_valid():
            #* save data
            account = serializer.save()
            # prepare main response
            data['response'] = 'Registro exitoso!!!'
            data['username'] = account.username
            data['email'] = account.email
            # get token
            refresh_token = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token)
            }
        else:
            return Response(serializer.errors)    
        
        return Response(data)
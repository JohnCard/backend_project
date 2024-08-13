from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError,CharField

class RegistrationSerializer(ModelSerializer):
    password_confirmation = CharField(
        style = {'input': 'password'}, write_only = True
    )
    
    class Meta:
        model = User
        fields=['username', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        # pull password
        password = self.validated_data['password']
        # pull password confirmation
        password_confirmation = self.validated_data['password_confirmation']
        # ? same passwords?
        if password != password_confirmation:
            # ! bad request
            raise ValidationError({'error': 'password and password_confirmation deben de ser iguales'})
        # pull email parameter
        email = self.validated_data['email']
        # ? exist email?
        if User.objects.filter(email=email).exists():
            # ! bad request
            raise ValidationError({'error': 'Correo ya en uso'})
        # get username
        username = self.validated_data['username']
        # create new user
        account = User(email=email, username=username)
        account.set_password(password)
        #* save data
        account.save()
        return account
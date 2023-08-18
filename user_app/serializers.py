from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError,CharField
from rest_framework.response import Response

class RegistrationSerializer(ModelSerializer):
    password2 = CharField(
        style={'input': 'password'},write_only=True
    )
    
    class Meta:
        model = User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise ValidationError({'error': 'password and password2 deben de ser comlpetamente identicas!!!'})
        
        email = self.validated_data['email']
        
        if User.objects.filter(email=email).exists():
            raise ValidationError({'error': 'Este correo ya fue usado, JODASE PENDJO PUTO!!!'})
        
        username = self.validated_data['username']
        
        account = User(email=email, username=username)
        account.set_password(password)
        account.save()
        
        return account
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime

class Programmer(serializers.Serializer):
    'Seriealiza un campo de nombre para nuestra APIView'
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=50)
    technology = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(datetime.now().strftime('%a, %d %b %Y %H:%M'))
    # id = serializers.ReadOnlyField()
    # first_name = serializers.CharField(max_length=15)
    # last_name = serializers.CharField()
    # username = serializers.CharField()
    # email = serializers.EmailField()
    # password = serializers.CharField()
    
    # def create(self, validated_data):
    #     instance = User()
    #     instance.first_name = validated_data.get('first_name')
    #     instance.last_name = validated_data.get('last_name')
    #     instance.username = validated_data.get('username')
    #     instance.email = validated_data.get('email')
    #     instance.set_password(validated_data.get('password'))
    #     instance.save()
    #     return instance
    
    # def validate_user_name(self, data):
    #     user = User.objects.filter(username=data)
    #     if len(user) != 0:
    #         raise serializers.ValidationError('Este nombre de usuario ya existe, ingrese otro nombre')
    #     else:
    #         return data

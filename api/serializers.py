from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )
        
class SecondProjectSerializer(serializers.Serializer):
    # id project
    id = serializers.IntegerField(label='Enter Id project')
    # title project
    title = serializers.CharField(label='Enter Project name')
    # description project
    description = serializers.CharField(label='Enter description')
    # technology project
    technology = serializers.CharField(label='Enter technology')
    
class ThirdProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
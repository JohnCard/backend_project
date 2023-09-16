from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )
        
class ProjectSerializerSc(serializers.Serializer):
    id=serializers.IntegerField(label='Enter Id project')
    title = serializers.CharField(label='Enter Project name')
    description = serializers.CharField(label='Enter description')
    technology = serializers.CharField(label='Enter technology')
    

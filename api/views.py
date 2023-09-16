from django.shortcuts import render
# Create your views here.
from rest_framework import views,status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer, ProjectSerializerSc

class ProductAPIView(views.APIView):
    
    def get(self,request):
        projects = Project.objects.all().values()
        return Response({'Message':'List of projects','List':projects})
    
    def post(self, request):
        serializer_pro = ProjectSerializerSc(data=request.data)
        if(serializer_pro.is_valid()):
            Project.objects.create(id=serializer_pro.data.get('id'),
                                   title=serializer_pro.data.get('title'),
                                   description=serializer_pro.data.get('description'),
                                   technology=serializer_pro.data.get('technology'))
        project = Project.objects.all().filter(id=request.data['id']).values()
        return Response({'Message':'New Done Project','Project':project})
    
    def put(self, request):
        content={
            'Youre calling a put method'
        }
        return Response(content)
    
    def patch(self, request):
        content={
            'Youre calling a pacth method'
        }
        return Response(content)
    
    def delete(self, request):
        content ={
            'Youre calling a delete method'
        }
        return Response(content)
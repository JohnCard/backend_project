from django.shortcuts import render
# Create your views here.
from rest_framework import views,status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer, ProjectSerializerSc
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

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
    
class ProjectThrd(views.APIView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id):
        if(id>0):
            project = list(Project.objects.filter(id=id).values())
            if(len(project)>0):
                proj = project[0]
                datos = {'message':'Succes','Projects':proj}
        else:
            projects = list(Project.objects.all().values())
            if len(projects) > 0:
                datos = {'message':'Succes','Projects':projects}
            else:
                datos = {'message':'Not found...'}
            return JsonResponse(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        Project.objects.create(id=jd['id'],title=jd['title'],description=jd['description'],technology=jd['technology'])
        data = {'Message':'Succes'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        project = list(Project.objects.filter(id=id).values())
        if len(project)>0:
            project = Project.objects.get(id=id)
            project.title = jd['title']
            project.description = jd['description']
            project.technology = jd['technology']
            project.save()
            data = {'Message':'Succes'}
        else:
            data = {'Message':'Failed'}
        return JsonResponse(data)
    
    def delete(self,request,id):
        project = list(Project.objects.filter(id=id).values())
        if len(project)>0:
            Project.objects.filter(id=id).delete()
            data = {'Message':'Succes'}
        else:
            data = {'Message':'Failed'}
        return JsonResponse(data)
            
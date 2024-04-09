from .models import Project
from rest_framework import viewsets, permissions, status
from .serializers import ProjectSerializer,ProjectSerializerSc
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import json
from django.http.response import JsonResponse
class ProjectView(viewsets.ModelViewSet):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
class ProjectViewSC(APIView):
    
    def get(self,request,id):
        if(id>0):
            project = list(Project.objects.filter(id=id).values())
            if(len(project)>0):
                proj = project[0]
                datos = {'message':'Succes','Projects':proj}
        else:
            datos = {'message':'Not found...'}
        return Response(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        Project.objects.create(id=jd['id'],title=jd['title'],description=jd['description'],technology=jd['technology'])
        data = {'Message':'Succes'}
        return Response(data)
    
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
        return Response(data)
    
    def delete(self,request,id):
        project = list(Project.objects.filter(id=id).values())
        if len(project)>0:
            Project.objects.filter(id=id).delete()
            data = {'Message':'Succes'}
        else:
            data = {'Message':'Failed'}
        return Response(data)
    
class ProjectViewSCND(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        projects = Project.objects.filter(user = self.request.user)
        return projects
    
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            projs_serializer = ProjectSerializer(self.get_queryset(),many=True)
            return Response(projs_serializer.data)
        else:
            return Response('Respuesta no validada')
            
    def retrieve(self, request, *args, **kwargs):
        try: 
            projects = Project.objects.filter(id=kwargs['pk'])
            serializer = ProjectSerializer(projects,many=True)
            return Response(serializer.data)
        except:
            return Response({'Message': 'We couldn´t ubicate this item'})
    
    def create(self, request, *args, **kwargs):
        project_data = request.data
        new_proj = Project.objects.create(title=project_data['title'],description=project_data['description'],technology=project_data['technology'])
        new_proj.save()
        serializer = ProjectSerializer(new_proj)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        try:
            comment_id = self.kwargs["pk"]
            comment = get_object_or_404(Project, id=comment_id)
            comment.delete()
            return Response({'Message': 'Object deleted successfully'})
        except:
            return Response({'Message':'we couldn´t get the item indicated'})
    
    def update(self, request, *args, **kwargs):
        proj = get_object_or_404(Project, id=self.kwargs["pk"])
        proj_serializer = ProjectSerializer(proj, data=request.data)
        if proj_serializer.is_valid():
            proj_serializer.save()
            return Response(proj_serializer.data)
        return Response({'Message': 'Failed request'})
    
    def partial_update(self, request, *args, **kwargs):
        proj_object = get_object_or_404(Project, id=self.kwargs["pk"])
        serializer = ProjectSerializer(proj_object, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(request.data)
        return Response("wrong parameters")

@api_view(['GET','POST','DELETE','PUT','PATCH'])
def fourth_project(request,pk=None):
    if request.method == 'GET':
        project = Project.objects.filter(id=pk).first()
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        project = Project.objects.filter(id=pk).first()
        serializer = ProjectSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        project = Project.objects.filter(id=pk).first()
        serializer = ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            return Response(request.data)
        return Response(serializer.errors)
    
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        project = Project.objects.filter(id=pk).first()
        project.delete()
        return Response('Deleted')
from .models import Project
from rest_framework import viewsets, permissions, status
from .serializers import ProjectSerializer,ProjectSerializerSc
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ProjectView(viewsets.ModelViewSet):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
class ProjectViewSC(APIView):
    
    def get(self,request,id):
        try:
            obj = Project.objects.get(id=id)
        except Project.DoesNotExist:
            msg = {'msg':'message not found'}
            return Response(msg,status.HTTP_404_NOT_FOUND)
        
        serializer = ProjectSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.data,status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        try:
            obj = Project.objects.get(id=id)
        except Project.DoesNotExist:
            msg = {'Message':'this item doesn´t exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProjectSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj = Project.objects.get(id=id)
        except Project.DoesNotExist:
            msg = {'Message':'this item doesn´t exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProjectSerializer(obj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        try:
            obj = Project.objects.get(id=id)
        except Project.DoesNotExist:
            msg = {'Message':'this item doesn´t exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'Message':'succesfully operation (deleted)'},status=status.HTTP_204_NO_CONTENT)
    
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

@api_view(['GET','POST','DELETE','PUT'])
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
from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser

class ProjectView(viewsets.ModelViewSet):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
class ProjectViewSCND(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        projects = Project.objects.filter(user = self.request.user)
        return projects
    
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            projs = self.get_queryset()
            projs_serializer = ProjectSerializer(projs,many=True)
            return Response(projs_serializer.data)
        else:
            return Response('Respuesta no validada')
            
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        projects = Project.objects.filter(id=params['pk'])
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        project_data = request.data
        
        new_proj = Project.objects.create(title=project_data['title'],description=project_data['description'],technology=project_data['technology'])
        print('solicitud exitosa :) !!!')
        new_proj.save()
        
        serializer = ProjectSerializer(new_proj)
        
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        comment_id = self.kwargs["pk"]
        comment = get_object_or_404(Project, id=comment_id)
        comment.delete()
        return Response({'Message': 'Object deleted successfully'})
    
    def update(self, request, *args, **kwargs):
        proj = get_object_or_404(Project, id=self.kwargs["pk"])
        proj_serializer = ProjectSerializer(proj, data=request.data)
        if proj_serializer.is_valid():
            proj_serializer.save()
            print('solicitud exitosa :)!!!')
            return Response(proj_serializer.data)
        return Response({'Message': 'Solicitud fracasada'})
    
    def partial_update(self, request, *args, **kwargs):
        proj_object = get_object_or_404(Project, id=self.kwargs["pk"])
        serializer = ProjectSerializer(proj_object, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(request.data)
        return Response("wrong parameters")
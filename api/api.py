# handle all your imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import json
from .models import Project
from .serializers import ProjectSerializer

# ModelViewSet project view
class ProjectModelViewSet(ModelViewSet):
    # define your queryset
    queryset = Project.objects.all()
    # define your serializer
    serializer_class = ProjectSerializer
    # define your permission classes
    permission_classes = [AllowAny]

class ProjectAPIView(APIView):
    def get(self, id):
        #? ¿exist id?
        if(id > 0):
            # pull project instances
            project = list(Project.objects.filter(id=id).values())
            #? ¿is not empty?
            if(len(project) > 0):
                proj = project[0]
                datos = {'message': 'Succes', 'Projects': proj}
        # it does exist!
        else:
            datos = {'message': 'Not found...'}
        return Response(datos)
    
    def post(self, request):
        # pull and convert json data
        jd = json.loads(request.body)
        # create instance
        Project.objects.create(id=jd['id'], title=jd['title'], description=jd['description'], technology=jd['technology'])
        # return succes message
        data = {'Message': 'Succes'}
        return Response(data)
    
    def put(self, request, id):
        # pull request data
        jd = json.loads(request.body)
        # filter instance
        project = list(Project.objects.filter(id=id).values())
        #? ¿is not empty?
        if len(project) > 0:
            project = Project.objects.get(id=id)
            project.title = jd['title']
            project.description = jd['description']
            project.technology = jd['technology']
            project.save()
            data = {'Message': 'Succes'}
        #! ¡something went wrong! 
        else:
            data = {'Message': 'Failed'}
        return Response(data)
    
    def delete(self, id):
        # filter instance by id
        project = list(Project.objects.filter(id=id).values())
        #? ¿existing instance?
        if len(project) > 0:
            # filter by id
            Project.objects.filter(id=id).delete()
            data = {'Message': 'Succes'}
        #! ¡something went wrong!
        else:
            data = {'Message': 'Failed'}
        return Response(data)
    
class ProjectSecondModelViewSet(ModelViewSet):
    # define your serializer
    serializer_class = ProjectSerializer
    
    # define your queryset
    def get_queryset(self):
        projects = Project.objects.filter(user = self.request.user)
        return projects
    
    def list(self, request, *args, **kwargs):
        # testing authentication
        if request.user.is_authenticated:
            # serialize authentication
            projs_serializer = ProjectSerializer(self.get_queryset(), many=True)
            return Response(projs_serializer.data)
        #! ¡bad request! 
        else:
            return Response('Respuesta no validada')
            
    def retrieve(self, request, *args, **kwargs):
        try: 
            # filter instance by id
            projects = Project.objects.filter(id=kwargs['pk'])
            # define your serializer
            serializer = ProjectSerializer(projects,many=True)
            return Response(serializer.data)
        except:
            return Response({'Message': 'We couldn´t ubicate this item'})
    
    def create(self, request, *args, **kwargs):
        # pull request data
        project_data = request.data
        # create a new instance
        new_proj = Project.objects.create(title=project_data['title'], description=project_data['description'],technology=project_data['technology'])
        new_proj.save()
        # return response
        serializer = ProjectSerializer(new_proj)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        try:
            # get id
            comment_id = self.kwargs["pk"]
            # get an instance or 404 error
            comment = get_object_or_404(Project, id=comment_id)
            comment.delete()
            return Response({'Message': 'Object deleted successfully'})
        #! bad request
        except:
            return Response({'Message': 'We couldn´t get the indicated item'})
    
    def update(self, request, *args, **kwargs):
        # get an instance or 404 error
        proj = get_object_or_404(Project, id=self.kwargs["pk"])
        # serialize data
        proj_serializer = ProjectSerializer(proj, data=request.data)
        #? valid data?
        if proj_serializer.is_valid():
            proj_serializer.save()
            return Response(proj_serializer.data)
        # ! not valid data
        return Response({'Message': 'Failed request'})
    
    def partial_update(self, request, *args, **kwargs):
        # get instance or 404 error
        proj_object = get_object_or_404(Project, id=self.kwargs["pk"])
        # serialize data
        serializer = ProjectSerializer(proj_object, data=request.data, partial=True)
        # ? valid data?
        if serializer.is_valid():
            return Response(request.data)
        # ! bad request
        return Response("wrong parameters")

@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def project_decorators(request, pk=None):
    # pull method
    method = request.method
    match method:
        case 'GET':
            # filter instance by id
            project = Project.objects.filter(id=pk).first()
            # serialize data
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        
        case 'PUT':
            # filter instance by id
            project = Project.objects.filter(id=pk).first()
            # serialize data
            serializer = ProjectSerializer(project,data=request.data)
            # ? valid data?
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # ! bad request
            return Response(serializer.errors)
        
        case 'PATCH':
            # filter instance by id
            project = Project.objects.filter(id=pk).first()
            # serialize data
            serializer = ProjectSerializer(project,data=request.data,partial=True)
            # ? valid data?
            if serializer.is_valid():
                return Response(request.data)
            # ! bad request
            return Response(serializer.errors)
        
        case 'POST':
            # serialize data
            serializer = ProjectSerializer(data=request.data)
            # valid data?
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # ! bad request
            return Response(serializer.errors)
        
        case 'DELETE':
            # filter instance by id
            project = Project.objects.filter(id=pk).first()
            # delete instance
            project.delete()
            return Response('Deleted')
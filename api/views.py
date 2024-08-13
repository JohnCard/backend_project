# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Project

class FirstProjectAPIView(APIView):
    
    def get(self, id):
        # retrieve one instance
        try:
            return Response({'Project': Project.objects.filter(id=id).values()})
        # return all project instances
        except:
            projects = Project.objects.all().values()
            return Response({'Message': 'List of projects', 'List': projects})
        finally:
            pass
    
    def post(self, request):
        return Response({'Message': request.data['title']})
    
    def put(self):
        content = {
            'Youre calling a put method'
        }
        return Response(content)
    
    def patch(self):
        content = {
            'Youre calling a pacth method'
        }
        return Response(content)
    
    def delete(self):
        content = {
            'Youre calling a delete method'
        }
        return Response(content)
    
class SecondProjectAPIView(APIView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, id):
        # ? exist id?
        if(id > 0):
            project = list(Project.objects.filter(id=id).values())
            # ? valid data?
            if(len(project) > 0):
                proj = project[0]
                datos = {'message': 'Succes', 'Projects': proj}
        # ! bad request
        else:
            datos = {'message': 'Not found...'}
            return JsonResponse(datos)
    
    def post(self, request):
        # pull data
        jd = json.loads(request.body)
        # create project instance
        Project.objects.create(id=jd['id'], title=jd['title'], description=jd['description'], technology=jd['technology'])
        # succes message
        data = {'Message': 'Succes'}
        return JsonResponse(data)
    
    def put(self, request, id):
        # pull and convert data
        jd = json.loads(request.body)
        # get project by id
        project = list(Project.objects.filter(id = id).values())
        # ? empty data?
        if len(project) > 0:
            #* pull main data
            project = Project.objects.get(id = id)
            project.title = jd['title']
            project.description = jd['description']
            project.technology = jd['technology']
            project.save()
            data = {'Message': 'Succes'}
        else:
            #! failed request
            data = {'Message': 'Failed'}
        return JsonResponse(data)
    
    def delete(self, id):
        # filter instance by id
        project = list(Project.objects.filter(id = id).values())
        # ? exist project?
        if len(project) > 0:
            # delete project
            Project.objects.filter(id = id).delete()
            data = {'Message': 'Succes'}
        # ! it doesn't exist
        else:
            data = {'Message': 'Failed'}
        return JsonResponse(data)
            
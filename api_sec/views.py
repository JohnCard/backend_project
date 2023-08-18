# Create your views here.
from .models import Project
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Programmer
from rest_framework import status
from rest_framework.viewsets import ViewSet
from django.db.models import Q

class TestAPIView(APIView):
    'API View de prueba'
    serializer_class = Programmer
    
    def get(self, request,format=None):
        'Regresa una lista de características de un APIView'
        apiview_info = [
            'Usa métodos HTTP como funciones (get, post, put, delete, patch)',
            'Es similar a un Django view tradicional',
            'Te da el mayor control de la lógica de la app',
            'Es mapeado manualmente a los urls'
        ]
        return Response({'message':'Hola','apiview_info':apiview_info})
    
    def post(self, request):
        'Crea un mensaje con el nombre ingresado'
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        'Manejar la actualización de un objeto'
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        'Manejar la actualización parcial de un objeto'
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        'Manejar la eliminación de un objeto'
        return Response({'method':'DELETE'})

class SecView(ViewSet):
    serializer_class = Programmer
    
    def list(self, request):
        'regresa un listado de características de los Viewsets'
        viewset_inf = [
            'Usa acciones, tales como list,create,retrieve,update,partial_update,destroy',
            'Se mapea automáticamente a los URLs usando routers',
            'Provee mayor funcionalidad con menos código'
            ]
        return Response({'message':'Hola','viewset_info': viewset_inf})
    
    def create(self,request):
        'Crea un mensaje de saludo'
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            # name = serializer.validated_data.get('first_name')
            # message = f'Hola {name}'
            Project.objects.create(title=serializer.validated_data.get('title'),description=serializer.validated_data.get('description'),technology=serializer.validated_data.get('technology'))
            return Response({'message':'Funcionó'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        'Maneja la consulta de un objeto a base de su identificador (id)'
        return Response({'Method':'GET'})
    
    def update(self, request, pk=None):
        'Maneja la actualización de un objeto a base de su identificador (id)'
        return Response({'Method':'PUT'})
    
    def partial_update(self, request, pk=None):
        'Maneja la actualización parcial de un objeto a base de su identificador (id)'
        return Response({'Method':'PATCH'})
    
    def destroy(self, request, pk=None):
        'Maneja la eliminación de un objeto a base de su identificador (id)'
        return Response({'Method':'DELETE'})
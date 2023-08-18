from django.shortcuts import render
# Create your views here.
from rest_framework import views
from rest_framework.response import Response

class ProductAPIView(views.APIView):
    
    def get(self, request):
        content ={
            'Youre calling a get method'
        }
        print(self.get)
        return Response(content)
    
    def post(self, request):
        content ={
            'request.POST.get '
        }
        print(self.post)
        return Response(content)
    
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
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#exportacion de serializer y modelos 
from Example2.models import Example2
from Example2.serializer import Ejemplo2Serializers

class Ejemplo2Lista(APIView):
    def get(self,request,format=None):
        print("hola get")
        queryset = Example2.objects.all()
        serializer = Ejemplo2Serializers(queryset,many = True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = Ejemplo2Serializers(data = request.data)
        print("post")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
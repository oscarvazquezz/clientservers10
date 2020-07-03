from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#exportacion de serializer y modelos 
from Example1.models import Example1
from Example1.serializer import Ejemplo1Serializers

class EjemploLista(APIView):
    def get(self,request,format=None):
        print("get")
        queryset = Example1.objects.all()
        serializer = Ejemplo1Serializers(queryset,many = True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = Ejemplo1Serializers(data = request.data)
        print("post")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)

class EjemploDetalle(APIView):
    def get_object(self,id):
        try:
            return Example1.objects.get(pk=id)
        except Example1.DoesNotExist:
            return 404

    def get(self,request,id,format=None):
        print("get detalle")
        ejemplo = self.get_object(id)
        if ejemplo == 404:
            return Response("lo siento no hay dato")
        else:
            serializer = Ejemplo1Serializers(ejemplo)
            return Response(serializer.data)
        
    def put(self,request,id,format=None):
        print("put detalle")
        idEjemplo = self.get_object(id)
        if idEjemplo == 404:
            return Response("lo siento no hay dato")
        else:
            serializer = Ejemplo1Serializers(idEjemplo,data=request.data)
            if serializer.is_valid():
                serializer.save()
                datos = serializer.data
                return Response(datos)
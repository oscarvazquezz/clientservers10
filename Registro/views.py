from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from Registro.serializer import RegistroSerializer

# Create your views here.

class RegistroUsuario(ObtainAuthToken,APIView):
    def get (self,request, format = None):
        queryset = User.objects.all() 
        serializer = RegistroSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self,request, format = None):
        serializer = RegistroSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            datas = serializer.data     
            token, created = Token.objects.get_or_create(user=user)
            return Response (datas, status = status.HTTP_201_CREATED)
        else :
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
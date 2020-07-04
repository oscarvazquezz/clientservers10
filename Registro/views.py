from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib.auth.models import User
from Registro.serializer import RegistroSerializers

# Create your views here.

class RegistroUsuario(ObtainAuthToken):
        
    
    def post(self,request,format=None):
        print("post")
        userRegistro = RegistroSerializers(data = request.data)
        print(userRegistro)
        users = User.objects.create_superuser(username = request.data,email = 'Sakura@gmail.com',password = request.data)
        print("saber")
        return Response({'ya quedo'})
        
from rest_framework import routers, serializers,viewsets 
from django.contrib.auth.models import User

class RegistroSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
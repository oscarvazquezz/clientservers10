from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from Example2 import views

urlpatterns = [
    re_path(r'/Example2/$',views.Ejemplo2Lista.as_view()),
]
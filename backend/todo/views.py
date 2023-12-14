from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 

from .models import TodoModel
from .serializers import TodoSerializer 

class TodoViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    



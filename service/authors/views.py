#from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ModelUser
from .serializers import ModelUserSerializer


class ModelUserViewSet(ModelViewSet):
    queryset = ModelUser.objects.all()
    serializer_class = ModelUserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class CarpetViewSet(viewsets.ModelViewSet):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializers

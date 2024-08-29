from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers


class CarpetViewSet(viewsets.ModelViewSet):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializers


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerilizers


class ReedViewSet(viewsets.ModelViewSet):
    queryset = Reed.objects.all()
    serializer_class = ReedSerilizers


class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializers

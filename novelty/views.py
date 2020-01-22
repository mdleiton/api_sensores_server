from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class NoveltyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Novelty.objects.all()
    serializer_class = NoveltySerializer

class NodeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class Notificaciones(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        nuevas = Novelty.objects.filter(send=False)
        enviar = Novelty.objects.filter(send=False)
        serializer = NoveltySerializer(enviar, many=True).data
        nuevas.update(send=True)
        return Response(serializer, status=status.HTTP_200_OK)
        

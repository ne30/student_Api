from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import studSerializer, stud2Serializer
from .models import stud
from rest_framework.response import Response

class studViewSet(viewsets.ModelViewSet):
    queryset = stud.objects.all().order_by('-date_joined')
    serializer_class = studSerializer


    def list(self, request, *args, **kwargs):
        temp = stud.objects.all()
        serializer = stud2Serializer(temp, many=True)
        return Response(serializer.data)
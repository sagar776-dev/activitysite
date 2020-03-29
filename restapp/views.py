from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import MonitorSerializer



class MonitorView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MonitorSerializer




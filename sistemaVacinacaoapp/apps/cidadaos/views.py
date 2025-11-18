from django.shortcuts import render
from rest_framework import viewsets
from .models import Cidadao
from .serializer import CidadaoSerializer

class CidadaoViewSet(viewsets.ModelViewSet):
    queryset = Cidadao.objects.all()
    serializer_class = CidadaoSerializer

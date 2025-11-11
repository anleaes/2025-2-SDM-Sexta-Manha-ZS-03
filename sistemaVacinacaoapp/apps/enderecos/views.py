from django.shortcuts import render
from rest_framework import viewsets
from .models import Endereco
from .serializer import EnderecosSerializer

class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
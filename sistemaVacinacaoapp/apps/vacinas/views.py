from django.shortcuts import render
from rest_framework import viewsets
from .models import Vacina
from .serializer import VacinaSerializer

class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer
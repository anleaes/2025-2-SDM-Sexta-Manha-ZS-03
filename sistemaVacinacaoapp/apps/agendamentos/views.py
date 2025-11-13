from django.shortcuts import render
from rest_framework import viewsets
from .models import Agendamento
from .serializer import AgendamentoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

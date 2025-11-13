from django.shortcuts import render
from rest_framework import viewsets
from .models import Agendamento
from .serializer import AgendamentoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

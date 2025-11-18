from django.shortcuts import render
from rest_framework import viewsets
from .models import Cartao
from .serializer import CartaoSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

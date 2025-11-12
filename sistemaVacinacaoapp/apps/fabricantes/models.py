from django.db import models
from enderecos.models import Enderecos

class Fabricante(models.Model):
    endereco = models.OneToOneField(Enderecos, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta: 
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering =['id']


    def __str__(self):
        return self.nome
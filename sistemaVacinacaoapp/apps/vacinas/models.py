from django.db import models
from fabricantes.models import Fabricante

class Vacina(models.Model):
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    doses = models.IntegerField()
    intervaloDias = models.IntegerField()
    doenca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
from django.db import models
from enderecos.models import Endereco
from unidades.models import Unidade

class Funcionario(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    cargo = models.CharField('Cargo', max_length=30, choices=[
        ('ENFERMEIRO', 'Enfermeiro'),
        ('MEDICO', 'Médico'),
        ('ADMINISTRATIVO', 'Administrativo'),
        ('OUTROS', 'Outros'),
        ])
    registro = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}, {self.cargo}."

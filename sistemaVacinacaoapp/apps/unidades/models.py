from django.db import models
from enderecos.models import Enderecos

class Unidade(models.Model):
    endereco = models.OneToOneField(Enderecos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    zona = models.CharField('Status', max_length=30, choices=[
        ('URBANA', 'Urbana'),
        ('RURAL', 'Rural'),
        ])
    telefone = models.CharField(max_length=20)
    tipo = models.CharField('Status', max_length=30, choices=[
        ('POSTO', 'Posto de Saúde'),
        ('HOSPITAL', 'Hospital'),
        ('CLINICA', 'Clínica'),
        ])
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering =['id']
        
    def __str__(self):
        return self.nome

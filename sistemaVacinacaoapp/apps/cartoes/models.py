from django.db import models

class Cartao(models.Model):
    numero = models.CharField('Numero', max_length=50, min_length=10, unique=True)
    criacao = models.DateField()
    zona = models.CharField('Zona', max_length=30, choices=[
        ('SUL', 'Sul'),
        ('NORTE', 'Norte'),
        ('LESTE', 'Leste'),
        ('OESTE', 'Oeste'),
        ])
    status = models.CharField('Status', max_length=30, choices=[
        ('ATIVO', 'Ativo'),
        ('BLOQUEADO', 'Bloqueado'),
        ])

    def __str__(self):
        return self.numero
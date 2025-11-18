from django.db import models

class Cidadao(models.Model):
    endereco = models.ManyToManyField('enderecos.Endereco')
    carteirinha = models.ForeignKey('cartoes.Cartao', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    nascimento = models.DateField()
    idade = models.IntegerField()

    class Meta: 
        verbose_name = 'Cidadao'
        verbose_name_plural = 'Cidadaos'
        ordering =['id']

    def __str__(self):
        return self.nome
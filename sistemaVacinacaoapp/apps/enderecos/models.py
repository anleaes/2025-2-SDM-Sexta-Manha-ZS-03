from django.db import models

class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=200)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado',max_length=2)
    bairro = models.CharField('Bairro', max_length=100)

    class Meta:
        verbose_name = 'Enderecos'
        verbose_name_plural = 'Enderecos'
        ordering =['id']

    def __str__(self):
        return f"{self.rua}, {self.bairro}. {self.cidade}-{self.estado}"
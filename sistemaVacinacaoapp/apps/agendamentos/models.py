from django.db import models

class Agendamento(models.Model):
    unidade = models.ForeignKey('unidades.Unidade', on_delete=models.CASCADE)
    vacina = models.ForeignKey('vacinas.Vacina', on_delete=models.CASCADE)
    cidadao = models.ForeignKey('cidadaos.Cidadao', on_delete=models.CASCADE)
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.CASCADE)

    dataMarcada = models.DateField()
    status = models.CharField('Status', max_length=30, choices=[
        ('AGENDADO', 'Agendado'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
        ])
    observacoes = models.TextField()
    prioridade = models.CharField('Status', max_length=30, choices=[
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
        ])
    
    class Meta: 
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        return f"{self.cidadao} - {self.dataMarcada} - {self.status}. Vacina: {self.vacina}"
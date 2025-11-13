from django.db import models

class Agendamento(models.Model):
    unidade = models.ForeignKey('unidade.Unidade', on_delete=models.CASCADE)
    vacina = models.ForeignKey('vacina.Vacina', on_delete=models.CASCADE)
    cidadao = models.ForeignKey('cidadao.Cidadao', on_delete=models.CASCADE)
    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.CASCADE)

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

    def __str__(self):
        return f"{self.cidadao} - {self.dataMarcada} - {self.status}. Vacina: {self.vacina}"
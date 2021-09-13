from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
import datetime
from django.core.validators import MinValueValidator

class Base(models.Model):
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Especialidade(Base):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome


class Medico(Base):
    nome = models.CharField('Nome', max_length=150)
    crm = models.BigIntegerField('CRM', unique=True)
    email = models.CharField('E-mail', max_length=150, blank=True)
    telefone = models.CharField('Telefone', max_length=15, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Horario(Base):
    horario = models.TimeField('Horário', auto_now=False, auto_now_add=False, unique=True)

    def __str__(self):
        return f'{self.horario}'


class Agenda(Base):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField('Data de Alocação', validators=[MinValueValidator(datetime.date.today)])
    horario = models.ManyToManyField(Horario)

    class Meta:
        unique_together = ('medico', 'dia',)

    def __str__(self):
        return f'{self.medico}, {self.dia}'


# class Consulta(Base):
#     agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     horario = models.TimeField('Horário')
#     data = models.DateField('Data do agendamento')

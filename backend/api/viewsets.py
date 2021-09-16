from rest_framework import viewsets
from backend.api import serializers
from backend.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters as filters_rest
from rest_framework.generics import ListAPIView, CreateAPIView
from backend.filters import *
from datetime import date, datetime
from django.db.models import Q
from django.db.models import F
from django_filters import rest_framework as filters

class EspecialidadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EspecialidadeSerializer
    queryset = Especialidade.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters_rest.SearchFilter]
    search_fields = ["^nome"]


class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicoSerializer
    queryset = Medico.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    # search_fields = ["^nome"]
    filterset_class = MedicoFilter


class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgendaSerializer
    def get_queryset(self):
        agendas = Agenda.objects.filter(dia__gte=date.today())
        existe_horario = False
        for agenda in agendas:
            for h in agenda.horario.all():
                # verifica se existe algum horário disponível na data atual
                if agenda.dia == date.today() and h.horario > datetime.now().time():
                    existe_horario = True
            if not existe_horario:
                agendas = agendas.exclude(id=agenda.id)

        return agendas

        # return agendas.exclude(Q(dia=date.today()) & Q(horario__horario__lt=datetime.now().time()))

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # pega as consultas do usuário logado com a data da consulta maior que a data atual
        consultas = Consulta.objects.filter(usuario=self.request.user, agenda__dia__gte=date.today())
        # No caso da data da consulta ser a mesma da data atual,
        # retorna apenas as consultas cujo horario agendado é maior que o horário atual
        return consultas.exclude(agenda__dia=date.today(), horario__horario__lt=datetime.now().time())

class UserViewSet(CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

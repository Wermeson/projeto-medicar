from rest_framework import viewsets
from backend.api import serializers
from backend.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters as filters_rest
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from backend.filters import *
from datetime import date, datetime
from django.db.models import Q
from django.db.models import F
from django_filters import rest_framework as filters
from drf_rw_serializers import generics

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
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AgendaFilter

    def get_queryset(self):
        agendas = Agenda.objects.filter(dia__gte=date.today())
        existe_horario_disponivel = False
        for agenda in agendas:
            existe_horario_disponivel = False
            for h in agenda.horario.all():
                # verifica se existe algum horário disponível na data atual e se existe alguma consulta naquele dia naquele horario
                if agenda.dia == date.today() and h.horario > datetime.now().time() and Consulta.objects.filter(agenda__dia=date.today(), horario__horario=h.horario).count() == 0:
                    existe_horario_disponivel = True
                # se a data da agenda é maior que a data atual, verifica se existe alguma consulta marcada na data a agenda no horario informado
                elif agenda.dia > date.today() and Consulta.objects.filter(agenda__dia=agenda.dia, horario__horario=h.horario).count() == 0:
                    existe_horario_disponivel = True
            # Se não existe nenhum horário disponivel naquela agenda, remove ela da listagem
            if not existe_horario_disponivel:
                agendas = agendas.exclude(id=agenda.id)

        return agendas

        # return agendas.exclude(Q(dia=date.today()) & Q(horario__horario__lt=datetime.now().time()))

class ConsultaViewSet(generics.ListCreateAPIView):
    read_serializer_class = serializers.ConsultaSerializer
    write_serializer_class = serializers.ConsultaCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # pega as consultas do usuário logado com a data da consulta maior que a data atual
        consultas = Consulta.objects.filter(usuario=self.request.user, agenda__dia__gte=date.today())
        # No caso da data da consulta ser a mesma da data atual,
        # retorna apenas as consultas cujo horario agendado é maior que o horário atual
        return consultas.exclude(agenda__dia=date.today(), horario__horario__lt=datetime.now().time())


class ConsultaDeleteViewSet(RetrieveDestroyAPIView):

    serializer_class = serializers.ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        consultas = Consulta.objects.filter(usuario=self.request.user)
        return consultas.filter(Q(agenda__dia__gt=date.today()) | (Q(agenda__dia=date.today()) & Q(horario__horario__gte=datetime.now().time())))


class UserViewSet(CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

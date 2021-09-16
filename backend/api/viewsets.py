from rest_framework import viewsets
from backend.api import serializers
from backend.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters as filters_rest
from rest_framework.generics import ListAPIView, CreateAPIView
from backend.filters import *
from datetime import date, datetime
from django.db.models import Q

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
    filter_backends = [filters_rest.SearchFilter]
    search_fields = ["^nome"]
    # filterset_class = MedicoFilter


class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgendaSerializer
    queryset = Agenda.objects.all()

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultaSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Consulta.objects.all()
    def get_queryset(self):
        consultas = Consulta.objects.filter(usuario=self.request.user, agenda__dia__gte=date.today())
        # for consulta in consultas:
        #     if consulta.agenda.dia == date.today() and consulta.horario.horario < datetime.now().time(0):
        return consultas.exclude(agenda__dia=date.today(), horario__horario__lt=datetime.now().time())

        # return Consulta.objects.filter(Q(usuario=self.request.user) & Q(agenda__dia__gte=date.today()) | (Q(agenda__dia=date.today()) & Q(horario__horario__gte=datetime.now().time())))


class UserViewSet(CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

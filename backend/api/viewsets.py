from rest_framework import viewsets
from backend.api import serializers
from backend.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters as filters_rest
from rest_framework.generics import ListAPIView
from backend.filters import *

class EspecialidadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EspecialidadeSerializer
    queryset = Especialidade.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters_rest.SearchFilter]
    search_fields = ["^nome"]


class MedicoViewSet(ListAPIView):
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
    queryset = Consulta.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

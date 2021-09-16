from rest_framework import serializers
from backend.models import *

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome', ]


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer()

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade', ]


class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horarios = serializers.SerializerMethodField()

    # Monta uma lista de horários disponiveis de acordo com os horários da agenda do médico
    def get_horarios(self, obj):
        horarios=[]
        for h in obj.horario.all():
            # verifica se existe uma consulta agendada e se os horários disponiveis da agenda é maior que o horário atual
            if Consulta.objects.filter(agenda=obj, horario=h).count() == 0 and h.horario.strftime("%H:%M") > datetime.datetime.now().strftime("%H:%M"):
                horarios.append(h.horario)
        return horarios

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios', ]

class ConsultaSerializer(serializers.ModelSerializer):
    horario = serializers.SerializerMethodField()
    dia = serializers.SerializerMethodField()
    # agenda = AgendaSerializer()
    medico = serializers.SerializerMethodField()

    def get_horario(self, obj):
        return obj.horario.horario

    def get_dia(self, obj):
        return obj.agenda.dia

    def get_medico(self, obj):
        return MedicoSerializer(obj.agenda.medico).data

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico', ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(validated_data.get("username"), validated_data.get("email"), validated_data.get("password"))


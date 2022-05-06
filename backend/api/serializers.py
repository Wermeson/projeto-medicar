from backend.models import *
from datetime import datetime, date
from rest_framework import serializers


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = [
            "id",
            "nome",
        ]


class MedicoSerializer(serializers.ModelSerializer):
    especialidade_id = serializers.IntegerField()

    class Meta:
        model = Medico
        fields = [
            "id",
            "crm",
            "nome",
            "especialidade_id",
        ]


class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horarios = serializers.SerializerMethodField()

    # Monta uma lista de horários disponiveis de acordo com os horários da agenda do médico
    def get_horarios(self, obj):
        horarios = []
        for h in obj.horario.all():
            if obj.dia > date.today():
                # verifica se existe uma consulta agendada
                if not Consulta.objects.filter(agenda=obj, horario=h).exists():
                    horarios.append(h.horario)
            elif obj.dia == date.today():
                # verifica se existe uma consulta agendada e se os horários disponiveis da agenda é maior que o horário atual
                if (
                    not Consulta.objects.filter(agenda=obj, horario=h).exists()
                    and h.horario > datetime.now().time()
                ):
                    horarios.append(h.horario)
        return horarios

    class Meta:
        model = Agenda
        fields = [
            "id",
            "medico",
            "dia",
            "horarios",
        ]


class ConsultaSerializer(serializers.ModelSerializer):
    horario = serializers.SerializerMethodField()
    dia = serializers.SerializerMethodField()
    medico = serializers.SerializerMethodField()

    def get_horario(self, obj):
        return obj.horario.horario

    def get_dia(self, obj):
        return obj.agenda.dia

    def get_medico(self, obj):
        return MedicoSerializer(obj.agenda.medico).data

    class Meta:
        model = Consulta
        fields = [
            "id",
            "dia",
            "horario",
            "data_agendamento",
            "medico",
        ]


class ConsultaCreateSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()

    def create(self, validated_data):
        usuario = self.context["request"].user
        agenda = Agenda.objects.get(id=validated_data.get("agenda_id"))
        horario = Horario.objects.get(horario=validated_data.get("horario"))
        return Consulta.objects.create(usuario=usuario, agenda=agenda, horario=horario)

    def validate(self, attrs):
        agenda = Agenda.objects.filter(id=attrs["agenda_id"])
        horario = Horario.objects.filter(horario=attrs["horario"])
        usuario = self.context["request"].user
        # Verifica se a agenda existe
        if not agenda.exists():
            raise serializers.ValidationError({"Agenda": "Essa agenda não existe!"})
        elif not horario.exists():
            raise serializers.ValidationError(
                {"Horário": "Esse horário não foi cadastrado"}
            )
        elif not agenda.filter(horario__horario=horario.get().horario).exists():
            raise serializers.ValidationError({"Horário": "Horário Indisponível"})
        elif (
            agenda.get().dia == date.today()
            and horario.get().horario < datetime.now().time()
        ):
            raise serializers.ValidationError({"Horário": "Esse horário já passou"})
        elif agenda.get().dia < date.today():
            raise serializers.ValidationError({"Data": "Data passada"})
        elif Consulta.objects.filter(
            usuario=usuario,
            agenda__dia=agenda.get().dia,
            horario__horario=horario.get().horario,
        ).exists():
            raise serializers.ValidationError(
                {"Consulta": "Já existe uma consulta cadastrada para esse horário"}
            )
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data.get("username"),
            validated_data.get("email"),
            validated_data.get("password"),
        )

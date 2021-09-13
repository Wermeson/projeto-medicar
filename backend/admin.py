from django.contrib import admin
from .models import *
# Register your models here.

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    list_filter = ["nome"]
    exclude = ['ativo', ]


admin.site.register(Especialidade, EspecialidadeAdmin)


class MedicoAdmin(admin.ModelAdmin):
    list_display = ["nome", "crm", "email", "telefone", "especialidade"]
    list_filter = ["nome", "especialidade"]
    exclude = ['ativo', ]


admin.site.register(Medico, MedicoAdmin)

class HorarioAdmin(admin.ModelAdmin):
    list_display = ["horario"]
    exclude = ['ativo', ]


admin.site.register(Horario, HorarioAdmin)


class AgendaAdmin(admin.ModelAdmin):
    list_display = ["medico", "dia", "get_horarios"]
    list_filter = ["medico", "dia",]
    exclude = ['ativo', ]

    @admin.display(description="Horários")
    def get_horarios(self, obj):
        horarios=[]
        for h in obj.horario.all():
            horarios.append(h)
        return horarios

admin.site.register(Agenda, AgendaAdmin)
# admin.site.register(Consulta)
# teste
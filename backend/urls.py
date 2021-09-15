from rest_framework import routers
from backend.api.viewsets import *
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# route = routers.DefaultRouter()
# route.register(r'especialidades', EspecialidadeViewSet, basename='Especialidades')
# # route.register(r'medicos', MedicoViewSet.as_view({'get':'list',}), basename='Medicos')
# route.register(r'agendas', AgendaViewSet, basename='Agendas')
# route.register(r'consultas', ConsultaViewSet, basename='Consultas')

urlpatterns = [
    # path('', include(route.urls)),
    path("especialidades/", EspecialidadeViewSet.as_view({'get': 'list'}), name="especialidades"),
    path("medicos/", MedicoViewSet.as_view(), name="medicos"),
    path("agendas/", AgendaViewSet.as_view({'get': 'list'}), name="agendas"),
    path("consultas/", ConsultaViewSet.as_view({'get': 'list'}), name="consultas"),
    path("users/", UserViewSet.as_view({'get': 'list'}), name="users"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
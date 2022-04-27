from backend.api.viewsets import *
from django.urls import path
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("especialidades/", EspecialidadeViewSet.as_view(), name="especialidades"),
    path("medicos/", MedicoViewSet.as_view({'get': 'list'}), name="medicos"),
    path("agendas/", AgendaViewSet.as_view({'get': 'list'}), name="agendas"),
    path("consultas/", ConsultaViewSet.as_view(), name="consultas"),
    path("consultas/<int:pk>/", ConsultaDeleteViewSet.as_view(), name="consulta_delete"),
    path("users/", UserViewSet.as_view(), name="users"),
    path("login/", views.obtain_auth_token),
]
urlpatterns = format_suffix_patterns(urlpatterns)

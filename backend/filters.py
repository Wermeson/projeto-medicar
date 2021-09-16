from django.core.exceptions import ValidationError
from django_filters import fields
from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget, SuffixedMultiWidget
from backend.models import *

class MedicoFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="nome", lookup_expr="istartswith")
    especialidade = filters.ModelMultipleChoiceFilter(
        field_name="especialidade", queryset=Especialidade.objects.all()
    )

    class Meta:
        model = Medico
        fields = ["search", "especialidade"]
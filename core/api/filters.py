from django_filters import FilterSet, ModelMultipleChoiceFilter
from core.base.models import Prefeitura, Proposta


class PropostaFilter(FilterSet):
    prefeitura = ModelMultipleChoiceFilter(
        field_name='prefeitura',
        to_field_name='id',
        queryset=Prefeitura.objects.all(),
    )

    class Meta:
        model = Proposta
        fields = ['prefeitura']

from django_filters import FilterSet, ModelMultipleChoiceFilter
from core.base.models import Prefeitura, Proposta, Convenio, Atividade, LicenciamentoAmbiental


class PropostaFilter(FilterSet):
    prefeitura = ModelMultipleChoiceFilter(
        field_name='prefeitura',
        to_field_name='id',
        queryset=Prefeitura.objects.all(),
    )

    class Meta:
        model = Proposta
        fields = ['prefeitura']


class ConvenioFilter(FilterSet):
    prefeitura = ModelMultipleChoiceFilter(
        field_name='proposta__prefeitura',
        to_field_name='id',
        queryset=Prefeitura.objects.all(),
    )

    class Meta:
        model = Convenio
        fields = ['prefeitura']


class AtividadeFilter(FilterSet):
    convenio = ModelMultipleChoiceFilter(
        field_name='convenio',
        to_field_name='id',
        queryset=Convenio.objects.all(),
    )

    class Meta:
        model = Atividade
        fields = ['convenio']


class LicenciamentoAmbientalFilter(FilterSet):
    convenio = ModelMultipleChoiceFilter(
        field_name='convenio',
        to_field_name='id',
        queryset=Convenio.objects.all(),
    )

    class Meta:
        model = LicenciamentoAmbiental
        fields = ['convenio']

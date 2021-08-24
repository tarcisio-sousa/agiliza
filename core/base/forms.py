from django import forms
from django.forms import ModelForm
from core.base.models import Proposta
from core.base.models import Convenio, Projeto, Item, Opcao, Alternativa, ItemAlternativa
from core.base.models import Atividade, LicenciamentoAmbiental, ProjetoControle, ProjetoControleItem


class PropostaForm(ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'
        widgets = {'valor_contrapartida': forms.TextInput() }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prefeitura'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['lei_complementar'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['valor_contrapartida'].widget.attrs.update({
            'class': 'form-control form-control-sm money'})
        self.fields['valor_contrapartida'].localize = True
        self.fields['valor_contrapartida'].widget.is_localized = True
        self.fields['objeto'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})


class PropostaArquivoExtratoForm(ModelForm):
    class Meta:
        model = Proposta
        fields = ['extrato', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConvenioArquivoExtratoForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['arquivo_extrato', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['data_prevista', 'responsavel', 'consideracoes', 'situacao', 'anexo', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['responsavel'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['consideracoes'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['consideracoes'].widget.attrs['rows'] = 3
        self.fields['situacao'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['anexo'].widget.attrs.update({'class': 'form-control form-control-sm'})


class LicenciamentoForm(ModelForm):
    class Meta:
        model = LicenciamentoAmbiental
        fields = ['data_prevista', 'responsavel', 'consideracoes', 'situacao', 'anexo', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['responsavel'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['consideracoes'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['consideracoes'].widget.attrs['rows'] = 3
        self.fields['situacao'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['anexo'].widget.attrs.update({'class': 'form-control form-control-sm'})


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})


class ProjetoControleForm(ModelForm):
    class Meta:
        model = ProjetoControle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orgao'].widget.attrs.update({'class': 'form-control custom-select'})
        self.fields['convenio'].widget.attrs.update({'class': 'form-control custom-select'})
        self.fields['projeto'].widget.attrs.update({'class': 'form-control custom-select'})


class ProjetoControleItemForm(ModelForm):
    class Meta:
        model = ProjetoControleItem
        # fields = '__all__'
        exclude = ('controle',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['alternativa'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['responsavel'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['observacoes'].widget.attrs['rows'] = 3
        self.fields['comentario'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['subitem'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['projeto'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['observacoes'].widget.attrs['rows'] = 3
        self.fields['opcao'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})


class OpcaoForm(ModelForm):
    class Meta:
        model = Opcao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})


class ItemAlternativaForm(ModelForm):
    class Meta:
        model = ItemAlternativa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'form-control'})
        self.fields['alternativa'].widget.attrs.update({'class': 'form-control custom-select'})

from django.forms import ModelForm
from core.base.models import Proposta
from core.base.models import Convenio, Projeto, Item, Opcao, Alternativa, ItemAlternativa
from core.base.models import Atividade, LicenciamentoAmbiental, ProjetoControle


class PropostaForm(ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prefeitura'].widget.attrs.update({'class': 'form-control custom-select'})
        self.fields['lei_complementar'].widget.attrs.update({'class': 'form-control'})
        self.fields['data'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_contrapartida'].widget.attrs.update({'class': 'form-control'})
        self.fields['objeto'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})


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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['convenio'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control'})
        self.fields['responsavel'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['consideracoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['situacao'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['anexo'].widget.attrs.update({'class': 'form-control'})


class LicenciamentoForm(ModelForm):
    class Meta:
        model = LicenciamentoAmbiental
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['convenio'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control'})
        self.fields['responsavel'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['consideracoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['situacao'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['anexo'].widget.attrs.update({'class': 'form-control'})


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orgao'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['convenio'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})


class ProjetoControleForm(ModelForm):
    class Meta:
        model = ProjetoControle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['alternativa'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['responsavel'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['comentario'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control'})


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        self.fields['subitem'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['projeto'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['opcao'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})


class OpcaoForm(ModelForm):
    class Meta:
        model = Opcao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['item'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})
        # self.fields['usuario'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        # self.fields['opcao'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})


class ItemAlternativaForm(ModelForm):
    class Meta:
        model = ItemAlternativa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'form-control'})
        self.fields['alternativa'].widget.attrs.update({'class': 'form-control custom-select custom-select-sm'})

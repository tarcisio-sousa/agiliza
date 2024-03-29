from django import forms
from django.forms import ModelForm
from core.base.models import Proposta, Servico
from core.base.models import Convenio, Projeto, Item, Opcao, Alternativa, ItemAlternativa, Protocolo
from core.base.models import Atividade, LicenciamentoAmbiental, ProjetoControle, ProjetoControleItem
from core.base.models import ExecucaoConcedente, ExecucaoConvenente


class PropostaForm(ModelForm):
    auto_complete_prefeitura = forms.CharField(max_length=250)

    class Meta:
        model = Proposta
        fields = '__all__'
        widgets = {
            'prefeitura': forms.HiddenInput(),
            'valor_convenio': forms.TextInput(),
            'valor_contrapartida': forms.TextInput(),
            'valor_repasse': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['auto_complete_prefeitura'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['lei_complementar'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['valor_convenio'].widget.attrs.update({
            'class': 'form-control form-control-sm money', 'onblur': 'calculaRepasse(this)'})
        self.fields['valor_convenio'].localize = True
        self.fields['valor_convenio'].widget.is_localized = True
        self.fields['valor_contrapartida'].widget.attrs.update({
            'class': 'form-control form-control-sm money', 'onblur': 'calculaRepasse(this)'})
        self.fields['valor_contrapartida'].localize = True
        self.fields['valor_contrapartida'].widget.is_localized = True
        self.fields['valor_repasse'].widget.attrs.update({
            'class': 'form-control form-control-sm money'})
        self.fields['valor_repasse'].localize = True
        self.fields['valor_repasse'].widget.is_localized = True
        self.fields['objeto'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})


class PropostaArquivoExtratoForm(ModelForm):
    class Meta:
        model = Proposta
        fields = ['extrato', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PropostaValorLiberado(ModelForm):
    class Meta:
        model = Proposta
        fields = ['valor_liberado', ]
        widgets = {
            'valor_liberado': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valor_liberado'].widget.attrs.update({
            'class': 'form-control form-control-sm money'})
        self.fields['valor_liberado'].localize = True
        self.fields['valor_liberado'].widget.is_localized = True


class ConvenioArquivoExtratoForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['arquivo_extrato', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConvenioAprovacaoLicitacaoForm(ModelForm):
    class Meta:
        model = Convenio
        fields = [
            'data_aceite_licitacao',
            'nome_empresa_contratada',
            'cnpj_empresa_contratada',
            'numero_contrato',
            'data_contrato',
            'vigencia_contrato',
            'valor_contrato']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valor_contrato'].widget.attrs.update({
            'class': 'form-control form-control-sm money'})
        self.fields['valor_contrato'].localize = True
        self.fields['valor_contrato'].widget.is_localized = True


class ConvenioRecursoContaForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['data_liberacao_recurso', 'valor_recurso', ]
        widgets = {
            'valor_recurso': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_liberacao_recurso'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['valor_recurso'].widget.attrs.update({
            'class': 'form-control form-control-sm money'})
        self.fields['valor_recurso'].localize = True
        self.fields['valor_recurso'].widget.is_localized = True


class ServicoForm(ModelForm):
    auto_complete_prefeitura = forms.CharField(max_length=250)
    auto_complete_responsavel = forms.CharField(max_length=250)

    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'prefeitura': forms.HiddenInput(),
            'responsavel': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['auto_complete_prefeitura'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['objeto'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['observacoes'].widget.attrs['rows'] = 3
        self.fields['auto_complete_responsavel'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})


class ProtocoloForm(ModelForm):
    class Meta:
        model = Protocolo
        fields = ['data_prevista', 'data_protocolado', 'responsavel', 'consideracoes', 'situacao', 'anexo', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['data_protocolado'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['responsavel'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['consideracoes'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['consideracoes'].widget.attrs['rows'] = 3
        self.fields['situacao'].widget.attrs.update({
            'class': 'form-control form-control-sm custom-select custom-select-sm'})
        self.fields['anexo'].widget.attrs.update({'class': 'form-control form-control-sm'})


class ProtocoloDadosBancariosForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['banco', 'agencia', 'conta', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['banco'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['agencia'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['conta'].widget.attrs.update({'class': 'form-control form-control-sm'})


class ProtocoloEmpresaContratadaForm(ModelForm):
    class Meta:
        model = Convenio
        fields = [
            'nome_empresa_contratada',
            'cnpj_empresa_contratada',
            'numero_contrato',
            'data_contrato',
            'vigencia_contrato',
            'valor_contrato'
        ]
        widgets = {
            'valor_contrato': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_empresa_contratada'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['cnpj_empresa_contratada'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['numero_contrato'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['data_contrato'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['vigencia_contrato'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['valor_contrato'].widget.attrs.update({'class': 'form-control form-control-sm money'})
        self.fields['valor_contrato'].localize = True
        self.fields['valor_contrato'].widget.is_localized = True


class ProtocoloExecucaoConvenenteForm(ModelForm):
    class Meta:
        model = ExecucaoConvenente
        exclude = ('convenio',)
        widgets = {
            'parcela': forms.TextInput(),
            'valor_pagamento': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parcela'].widget.attrs.update({
            'class': 'form-control form-control-sm'
        })
        self.fields['data_pagamento'].widget.attrs.update({
            'class': 'form-control form-control-sm date'
        })
        self.fields['valor_pagamento'].widget.attrs.update({
            'class': 'form-control form-control-sm money'
        })
        self.fields['valor_pagamento'].localize = True
        self.fields['valor_pagamento'].widget.is_localized = True


class ProtocoloExecucaoConcedenteForm(ModelForm):
    class Meta:
        model = ExecucaoConcedente
        exclude = ('convenio',)
        widgets = {
            'parcela': forms.TextInput(),
            'valor_pagamento': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parcela'].widget.attrs.update({
            'class': 'form-control form-control-sm'
        })
        self.fields['data_liberacao'].widget.attrs.update({
            'class': 'form-control form-control-sm date'
        })
        self.fields['valor_pagamento'].widget.attrs.update({
            'class': 'form-control form-control-sm money'
        })
        self.fields['valor_pagamento'].localize = True
        self.fields['valor_pagamento'].widget.is_localized = True


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['data_prevista', 'data_protocolado', 'responsavel', 'consideracoes', 'situacao', 'anexo', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['data_protocolado'].widget.attrs.update({'class': 'form-control form-control-sm date'})
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
        fields = ['data_prevista', 'data_protocolado', 'responsavel', 'consideracoes', 'situacao', 'anexo', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_prevista'].widget.attrs.update({'class': 'form-control form-control-sm date'})
        self.fields['data_protocolado'].widget.attrs.update({'class': 'form-control form-control-sm date'})
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

    def __init__(self, projeto, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subitem'].queryset = Item.objects.filter(projeto=projeto)
        self.fields['descricao'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['descricao'].widget.attrs['rows'] = 3
        self.fields['subitem'].widget.attrs.update({
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

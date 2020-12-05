from django import forms
from django.forms import ModelForm
from core.base.models import Proposta, ProjetoPavimentacao


class PropostaForm(ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prefeitura'].widget.attrs.update({'class': 'form-control custom-select'})
        self.fields['lei_complementar'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_lei'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_contrapartida'].widget.attrs.update({'class': 'form-control'})
        self.fields['objeto'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})


class ProjetoPavimentacaoForm(ModelForm):
    class Meta:
        model = ProjetoPavimentacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CHOICES = [('1', 'Sim'), ('2', 'Não'), ('3', 'Dispensado')]
        CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA = [
            ('1', 'Sim (no caso de faltar algum documento comentar)'), ('2', 'Não, pelos seguintes motivos')]
        CHOICES_SERVICO_TERCEIRIZADO = [('1', 'Sim, com prazo de execução de'), ('2', 'Não')]
        self.fields['copia_plano_trabalho'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['qci'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['planta_georreferenciada'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['projeto_geometrico_planta_baixa'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['projeto_geometrico_perfil_longitudinal'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['projeto_terraplenagem_notas_servico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['projeto_terraplenagem_relatorio_volumes'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['projeto_terraplenagem_secoes_transversais'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['projeto_pavimentacao_secao_tipo'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['projeto_drenagem'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['projeto_sinalizacao_viaria'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['projeto_calcadas_acessibilidade'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['memorial_descritivo_projeto'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['especificacoes_tecnicas'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['orcamentos_detalhados'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['composicoes_custos_unitarios'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['detalhamento_bdi'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['cronograma_fisico_financeiro_empreendimento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['memoria_calculo_dimensionamento'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['declaracao_bem_uso_comum_povo'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['art_projeto'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['art_orcamento'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['art_acessibilidade'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['declaracao_munutencao_conservacao'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['declaracao_existencia_rede_abastecimento_agua'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['declaracao_existencia_solucao_esgotamento_sanitario'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['declaracao_regime_execucao_obra'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['equipe_coordenacao_projeto'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['contrato_elaboracao_projeto_engenharia'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['declaracao_autor_projeto_sinalizacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES
        )
        self.fields['relatorio_fotografico'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        self.fields['servico_apto_para_analise_tecnica'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA
        )
        self.fields['servico_terceirizado'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_TERCEIRIZADO
        )
        self.fields['sr'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_contrato'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_assinatura'].widget.attrs.update({'class': 'form-control'})
        self.fields['programa'].widget.attrs.update({'class': 'form-control'})
        self.fields['modalidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['proponente'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo_proponente'].widget.attrs.update({'class': 'form-control'})
        self.fields['empreendimento'].widget.attrs.update({'class': 'form-control'})
        self.fields['localizacao'].widget.attrs.update({'class': 'form-control'})
        self.fields['objetivo_pleito'].widget.attrs.update({'class': 'form-control'})
        self.fields['comentario_analise_tecnica'].widget.attrs.update({'class': 'form-control'})
        self.fields['justificativa_comentarios'].widget.attrs.update({'class': 'form-control'})
        self.fields['atividade'].widget.attrs.update({'class': 'form-control'})
        self.fields['produto'].widget.attrs.update({'class': 'form-control'})
        self.fields['linha'].widget.attrs.update({'class': 'form-control'})
        self.fields['fonte'].widget.attrs.update({'class': 'form-control'})
        self.fields['responsavel_verificacao'].widget.attrs.update({'class': 'form-control'})
        self.fields['data'].widget.attrs.update({'class': 'form-control'})
        self.fields['local_data'].widget.attrs.update({'class': 'form-control'})
        self.fields['responsavel_tecnico'].widget.attrs.update({'class': 'form-control'})
        self.fields['matricula'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['crea'].widget.attrs.update({'class': 'form-control'})

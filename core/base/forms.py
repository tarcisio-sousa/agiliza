from django import forms
from django.forms import ModelForm
from core.base.models import Proposta, Edificacao, Estrada, Equipamento, Pavimentacao, Convenio


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


class ConvenioArquivoExtratoForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['arquivo_extrato', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EdificacaoForm(ModelForm):
    class Meta:
        model = Edificacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        SIM = '1'
        NAO = '2'
        DISPENSADO = '0'
        CHOICES = [(SIM, 'Sim'), (NAO, 'Não'), (DISPENSADO, 'Dispensado')]
        self.fields['copia_plano_trabalho'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['existem_obras_iniciadas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['valores_investimento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['qci'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['planta_localizacao_empreendimento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_tecnico_pecas_graficas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['arquitetura'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_instalacoes_eletricas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_instalacoes_hidraulicas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_instalacoes_sanitarias'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_instalacoes_logica_telefonicas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_instalacoes_aguas_pluviais'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_instalacoes_combate_incendio_panico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_sistema_prevencao_descargas_atmosfericas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_acessibilidade'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_estrutural'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['levantamento_topografico_area_intervencao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['elemento_descritivo_projeto_basico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['memorial_descritivo'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['especificacoes_tecnicas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['orcamentos_detalhados'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['detalhamento_bdi'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['composicoes_custos_unitarios'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['cronograma_fisico_financeiro_individual'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['cronograma_fisico_financeiro'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['memoria_calculo_dimensionamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['teste_absorcao_percolacao_terreno'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['relatorio_sondagem'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['matricula_certidao_terreno_registro_imoveis'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['opcao_compra_venda_terreno'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_dominio_publico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['termo_doacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['aprovacao_projetos_orgaos_competentes'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['anotacao_responsabilidade_tecnica_art'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto_arquitetonico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto_instalacoes_hidrosanitarias'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto_instalacoes_eletricas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto_combate_incendio_spda'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_orcamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_acessibilidade'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_execucao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_fiscalizacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracoes_orgaos_competentes'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_manutencao_conservacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_viabilidade_fornecimento_energia'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_viabilidade_fornecimento_agua'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_viabilidade_atendimento_rede_esgosto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_viabilidade_coleta_lixo'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['manifestacao_orgao_meio_ambiente'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['licenca_previa'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['licenca_instalacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['licenca_operacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['dispensa_licenciamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['equipe_coordenacao_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_execucao_obra'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_contrapartida'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['contrato_projeto_engenharia'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['relatorio_fotografico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
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


class EquipamentoForm(ModelForm):
    class Meta:
        model = Estrada
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        SIM = '1'
        NAO = '2'
        DISPENSADO = '0'
        CHOICES = [(SIM, 'Sim'), (NAO, 'Não'), (DISPENSADO, 'Dispensado')]
        CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA = [
            ('1', 'Sim (no caso de faltar algum documento comentar)'), ('2', 'Não, pelos seguintes motivos')]
        CHOICES_SERVICO_TERCEIRIZADO = [('1', 'Sim, com prazo de execução de'), ('2', 'Não')]
        self.fields['copia_plano_trabalho'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['qci'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['especificacoes_detalhadas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['orcamentos_detalhados'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['cotacao_mercado'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['cronograma_fisico_financeiro_empreendimento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['plano_uso_equipamentos_adquiridos'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['documento_titularidade_area'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_orcamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_munutencao_conservacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_viabilidade_forneceimento_energia'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_viabilidade_forneceimento_agua'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_aquisicao_equipamentos'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['equipe_coordenacao_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['servico_apto_para_analise_tecnica'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA, initial=NAO)
        self.fields['servico_terceirizado'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_TERCEIRIZADO, initial=NAO)
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


class EstradaForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        SIM = '1'
        NAO = '2'
        DISPENSADO = '0'
        CHOICES = [(SIM, 'Sim'), (NAO, 'Não'), (DISPENSADO, 'Dispensado')]
        CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA = [
            ('1', 'Sim (no caso de faltar algum documento comentar)'), ('2', 'Não, pelos seguintes motivos')]
        CHOICES_SERVICO_TERCEIRIZADO = [('1', 'Sim, com prazo de execução de'), ('2', 'Não')]
        self.fields['copia_plano_trabalho'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['qci'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['planta_georreferenciada'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_geometrico_planta_baixa'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_geometrico_perfil_longitudinal'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_terraplenagem_notas_servico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_terraplenagem_relatorio_volumes'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_terraplenagem_secoes_transversais'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_pavimentacao_secao_tipo'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_drenagem'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_sinalizacao_viaria'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['planta_localizacao_jazida_fonte_agua'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['memorial_descritivo_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['especificacoes_tecnicas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['orcamentos_detalhados'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['composicoes_custos_unitarios'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['detalhamento_bdi'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['cronograma_fisico_financeiro_empreendimento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['memoria_calculo_dimensionamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_bem_uso_comum_povo'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_orcamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_munutencao_conservacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_regime_execucao_obra'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['equipe_coordenacao_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['contrato_elaboracao_projeto_engenharia'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['servico_apto_para_analise_tecnica'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA, initial=NAO)
        self.fields['servico_terceirizado'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_TERCEIRIZADO, initial=NAO)
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


class PavimentacaoForm(ModelForm):
    class Meta:
        model = Pavimentacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        SIM = '1'
        NAO = '2'
        DISPENSADO = '0'
        CHOICES = [(SIM, 'Sim'), (NAO, 'Não'), (DISPENSADO, 'Dispensado')]
        CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA = [
            ('1', 'Sim (no caso de faltar algum documento comentar)'), ('2', 'Não, pelos seguintes motivos')]
        CHOICES_SERVICO_TERCEIRIZADO = [('1', 'Sim, com prazo de execução de'), ('2', 'Não')]
        self.fields['copia_plano_trabalho'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['qci'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['planta_georreferenciada'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_geometrico_planta_baixa'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_geometrico_perfil_longitudinal'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_terraplenagem_notas_servico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_terraplenagem_relatorio_volumes'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_terraplenagem_secoes_transversais'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_pavimentacao_secao_tipo'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_drenagem'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_sinalizacao_viaria'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['projeto_calcadas_acessibilidade'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['memorial_descritivo_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['especificacoes_tecnicas'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['orcamentos_detalhados'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['composicoes_custos_unitarios'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['detalhamento_bdi'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['cronograma_fisico_financeiro_empreendimento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['memoria_calculo_dimensionamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_bem_uso_comum_povo'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_orcamento'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['art_acessibilidade'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_munutencao_conservacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_existencia_rede_abastecimento_agua'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_existencia_solucao_esgotamento_sanitario'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_regime_execucao_obra'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['equipe_coordenacao_projeto'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['contrato_elaboracao_projeto_engenharia'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['declaracao_autor_projeto_sinalizacao'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['relatorio_fotografico'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES, initial=NAO)
        self.fields['servico_apto_para_analise_tecnica'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_APTO_PARA_ANALISE_TECNICA, initial=NAO)
        self.fields['servico_terceirizado'] = forms.ChoiceField(
            widget=forms.RadioSelect, choices=CHOICES_SERVICO_TERCEIRIZADO, initial=NAO)
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

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cliente(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    cnpj = models.CharField(_('CNPJ'), max_length=20, blank=False, null=False)

    endereco = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(_('CEP'), max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    uf = models.CharField(_('UF'), max_length=5, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)


class Prefeitura(Cliente):
    # campo do tipo imagem, com o modelo de papel timbrado da prefeitura
    timbre = models.ImageField(upload_to='uploads/%Y/%m/%d', max_length=150)

    prefeito = models.ForeignKey('Prefeito', on_delete=models.CASCADE, blank=False, null=False)
    secretario_obras = models.ForeignKey('SecretarioDeObras', on_delete=models.CASCADE, blank=True, null=True)
    secretario_financeiro = models.ForeignKey('SecretarioFinanceiro', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(_('CPF'), max_length=20, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'profissional'
        verbose_name_plural = 'profissionais'

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = _('cargo')
        verbose_name_plural = _('cargos')

    def __str__(self):
        return self.descricao


class Prefeito(Profissional):

    class Meta:
        verbose_name = _('prefeito')
        verbose_name_plural = _('prefeitos')


class SecretarioDeObras(Profissional):

    class Meta:
        verbose_name = _('secretário de obras')
        verbose_name_plural = _('secretários de obras')


class SecretarioFinanceiro(Profissional):

    class Meta:
        verbose_name = _('secretário financeiro')
        verbose_name_plural = _('secretários financeiro')


class Proposta(models.Model):

    class SituacaoChoice(models.TextChoices):
        EM_ANALISE = 'em-analise', _('Em análise')
        EMPENHADO = 'empenhada', _('Empenhada')
        APROVADO = 'aprovada', _('Aprovada')
        REPROVADO = 'reprovada', _('Reprovada')

    prefeitura = models.ForeignKey('Prefeitura', on_delete=models.CASCADE, blank=False, null=False)
    lei_complementar = models.CharField(max_length=200, blank=False, null=False)
    data = models.DateField(_('Data'), blank=False, null=False)
    valor_contrapartida = models.FloatField(_('Valor da contrapartida'), blank=False, null=False)
    objeto = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(_('Número da proposta'), max_length=150, blank=False, null=False)
    situacao = models.CharField(
        max_length=15, choices=SituacaoChoice.choices, default=SituacaoChoice.EM_ANALISE, blank=True, null=True
    )
    extrato = models.FileField(upload_to='uploads/files/%Y/%m/%d', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _('proposta')
        verbose_name_plural = _('propostas')

    def __str__(self):
        return f'{self.numero} {self.objeto}'

    def verifica_situacao(self):
        if self.SituacaoChoice.EM_ANALISE == self.situacao:
            return self.SituacaoChoice.APROVADO
        if self.SituacaoChoice.APROVADO == self.situacao:
            return self.SituacaoChoice.EMPENHADO

        # return self.situacao
        # if (self.situacao == 'em-analise'):
        #     return SituacaoChoice.EMPENHADO
        # elif (self.situacao == 'empenhada'):
        #     return SituacaoChoice.APROVADO


class Convenio(models.Model):
    proposta = models.ForeignKey('Proposta', on_delete=models.CASCADE, blank=True, null=True)
    orgao = models.ForeignKey('Orgao', on_delete=models.CASCADE, blank=True, null=True)
    arquivo_extrato = models.FileField(upload_to='uploads/%Y/%m/%d', max_length=150, blank=True, null=True)
    numero_convenio = models.CharField(_('Número convênio (SICONV)'), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _('convênio')
        verbose_name_plural = _('convênios')

    def __str__(self):
        return f'{self.proposta}'


class Orgao(models.Model):
    descricao = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = _('orgão')
        verbose_name_plural = _('orgãos')

    def __str__(self):
        return f'{self.descricao}'


class Projeto(models.Model):
    class TipoChoice(models.TextChoices):
        ESTRADAS = 'estradas', _('Estradas')
        EQUIPAMENTO = 'equipamento', _('Equipamento')
        PAVIMENTACAO = 'pavimentacao', _('Pavimentacao')

    orgao = models.ForeignKey('Orgao', on_delete=models.CASCADE, blank=True, null=True)
    convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(
        max_length=150, choices=TipoChoice.choices, default=None, blank=True, null=True)

    def __str__(self):
        return f'Projeto {self.id}'


class Protocolo(models.Model):
    descricao = models.CharField(max_length=250, blank=False, null=False)
    data = models.DateField(_('Data'), auto_now=True, blank=False, null=False)
    arquivo = models.FileField(upload_to='uploads/%Y/%m/%d', max_length=150, blank=True, null=True)
    convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.data} - {self.descricao}'


class Edificacao(Projeto):
    # 1 - Identificação
    sr = models.CharField(max_length=250, blank=True, null=True)
    numero_contrato = models.CharField(max_length=250, blank=True, null=True)
    data_assinatura = models.CharField(max_length=250, blank=True, null=True)
    programa = models.CharField(max_length=250, blank=True, null=True)
    modalidade = models.CharField(max_length=250, blank=True, null=True)
    proponente = models.CharField(max_length=250, blank=True, null=True)
    tipo_proponente = models.CharField(max_length=250, blank=True, null=True)
    empreendimento = models.CharField(max_length=250, blank=True, null=True)
    localizacao = models.CharField(max_length=250, blank=True, null=True)

    # 2 - Objetivo
    objetivo_pleito = models.CharField(max_length=250, blank=True, null=True)

    # 3 - Documentação fornecida para a análise técnica do empreendimento
    copia_plano_trabalho = models.CharField(max_length=250, blank=True, null=True)
    existem_obras_iniciadas = models.CharField(max_length=250, blank=True, null=True)
    valores_investimento = models.CharField(max_length=250, blank=True, null=True)
    qci = models.CharField(max_length=250, blank=True, null=True)
    planta_localizacao_empreendimento = models.CharField(max_length=250, blank=True, null=True)
    projeto_tecnico_pecas_graficas = models.CharField(max_length=250, blank=True, null=True)
    arquitetura = models.CharField(max_length=250, blank=True, null=True)
    projeto_instalacoes_eletricas = models.CharField(max_length=250, blank=True, null=True)
    projeto_instalacoes_hidraulicas = models.CharField(max_length=250, blank=True, null=True)
    projeto_instalacoes_sanitarias = models.CharField(max_length=250, blank=True, null=True)
    projeto_instalacoes_logica_telefonicas = models.CharField(max_length=250, blank=True, null=True)
    projeto_instalacoes_aguas_pluviais = models.CharField(max_length=250, blank=True, null=True)
    projeto_instalacoes_combate_incendio_panico = models.CharField(max_length=250, blank=True, null=True)
    projeto_sistema_prevencao_descargas_atmosfericas = models.CharField(max_length=250, blank=True, null=True)
    projeto_acessibilidade = models.CharField(max_length=250, blank=True, null=True)
    projeto_estrutural = models.CharField(max_length=250, blank=True, null=True)
    levantamento_topografico_area_intervencao = models.CharField(max_length=250, blank=True, null=True)
    elemento_descritivo_projeto_basico = models.CharField(max_length=250, blank=True, null=True)
    memorial_descritivo = models.CharField(max_length=250, blank=True, null=True)
    especificacoes_tecnicas = models.CharField(max_length=250, blank=True, null=True)
    orcamentos_detalhados = models.CharField(max_length=250, blank=True, null=True)
    detalhamento_bdi = models.CharField(max_length=250, blank=True, null=True)
    composicoes_custos_unitarios = models.CharField(max_length=250, blank=True, null=True)
    cronograma_fisico_financeiro_individual = models.CharField(max_length=250, blank=True, null=True)
    cronograma_fisico_financeiro = models.CharField(max_length=250, blank=True, null=True)
    memoria_calculo_dimensionamento = models.CharField(max_length=250, blank=True, null=True)
    teste_absorcao_percolacao_terreno = models.CharField(max_length=250, blank=True, null=True)
    relatorio_sondagem = models.CharField(max_length=250, blank=True, null=True)
    matricula_certidao_terreno_registro_imoveis = models.CharField(max_length=250, blank=True, null=True)
    opcao_compra_venda_terreno = models.CharField(max_length=250, blank=True, null=True)
    declaracao_dominio_publico = models.CharField(max_length=250, blank=True, null=True)
    termo_doacao = models.CharField(max_length=250, blank=True, null=True)
    aprovacao_projetos_orgaos_competentes = models.CharField(max_length=250, blank=True, null=True)
    anotacao_responsabilidade_tecnica_art = models.CharField(max_length=250, blank=True, null=True)
    art_projeto_arquitetonico = models.CharField(max_length=250, blank=True, null=True)
    art_projeto_instalacoes_hidrosanitarias = models.CharField(max_length=250, blank=True, null=True)
    art_projeto_instalacoes_eletricas = models.CharField(max_length=250, blank=True, null=True)
    art_projeto_combate_incendio_spda = models.CharField(max_length=250, blank=True, null=True)
    art_orcamento = models.CharField(max_length=250, blank=True, null=True)
    art_acessibilidade = models.CharField(max_length=250, blank=True, null=True)
    art_execucao = models.CharField(max_length=250, blank=True, null=True)
    art_fiscalizacao = models.CharField(max_length=250, blank=True, null=True)
    declaracoes_orgaos_competentes = models.CharField(max_length=250, blank=True, null=True)
    declaracao_manutencao_conservacao = models.CharField(max_length=250, blank=True, null=True)
    declaracao_viabilidade_fornecimento_energia = models.CharField(max_length=250, blank=True, null=True)
    declaracao_viabilidade_fornecimento_agua = models.CharField(max_length=250, blank=True, null=True)
    declaracao_viabilidade_atendimento_rede_esgosto = models.CharField(max_length=250, blank=True, null=True)
    declaracao_viabilidade_coleta_lixo = models.CharField(max_length=250, blank=True, null=True)
    manifestacao_orgao_meio_ambiente = models.CharField(max_length=250, blank=True, null=True)
    licenca_previa = models.CharField(max_length=250, blank=True, null=True)
    licenca_instalacao = models.CharField(max_length=250, blank=True, null=True)
    licenca_operacao = models.CharField(max_length=250, blank=True, null=True)
    dispensa_licenciamento = models.CharField(max_length=250, blank=True, null=True)

    # - Outros documentos
    equipe_coordenacao_projeto = models.CharField(max_length=250, blank=True, null=True)
    declaracao_execucao_obra = models.CharField(max_length=250, blank=True, null=True)
    declaracao_contrapartida = models.CharField(max_length=250, blank=True, null=True)
    contrato_projeto_engenharia = models.CharField(max_length=250, blank=True, null=True)
    relatorio_fotografico = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'projeto de edificacao'
        verbose_name_plural = 'projetos de edificacao'

    def __str__(self):
        return f'Projeto de edificacao Nº {self.id}'


class Praca(Edificacao):
    class Meta:
        verbose_name='praça'
        verbose_name_plural='praças'

    def __str__(self):
        return f'Projeto de praça Nº {self.id}'


class CentroEsportivo(Edificacao):
    class Meta:
        verbose_name='projeto de centro esportivo'
        verbose_name_plural='projetos de centros esportivo'

    def __str__(self):
        return f'Projeto de centro esportivo Nº {self.id}'


class Estrada(Projeto):
    # 1 - Identificação
    sr = models.CharField(max_length=250, blank=True, null=True)
    numero_contrato = models.CharField(max_length=250, blank=True, null=True)
    data_assinatura = models.CharField(max_length=250, blank=True, null=True)
    programa = models.CharField(max_length=250, blank=True, null=True)
    modalidade = models.CharField(max_length=250, blank=True, null=True)
    proponente = models.CharField(max_length=250, blank=True, null=True)
    tipo_proponente = models.CharField(max_length=250, blank=True, null=True)
    empreendimento = models.CharField(max_length=250, blank=True, null=True)
    localizacao = models.CharField(max_length=250, blank=True, null=True)

    # 2 - Objetivo
    objetivo_pleito = models.CharField(max_length=250, blank=True, null=True)

    # 3 - Documentação fornecida para a análise técnica do empreendimento
    copia_plano_trabalho = models.CharField(max_length=250, blank=True, null=True)
    qci = models.CharField(max_length=250, blank=True, null=True)
    planta_georreferenciada = models.CharField(max_length=250, blank=True, null=True)
    projeto_geometrico_planta_baixa = models.CharField(max_length=250, blank=True, null=True)
    projeto_geometrico_perfil_longitudinal = models.CharField(max_length=250, blank=True, null=True)
    projeto_terraplenagem_notas_servico = models.CharField(max_length=250, blank=True, null=True)
    projeto_terraplenagem_relatorio_volumes = models.CharField(max_length=250, blank=True, null=True)
    projeto_terraplenagem_secoes_transversais = models.CharField(max_length=250, blank=True, null=True)
    projeto_pavimentacao_secao_tipo = models.CharField(max_length=250, blank=True, null=True)
    projeto_drenagem = models.CharField(max_length=250, blank=True, null=True)
    projeto_sinalizacao_viaria = models.CharField(max_length=250, blank=True, null=True)
    planta_localizacao_jazida_fonte_agua = models.CharField(max_length=250, blank=True, null=True)
    memorial_descritivo_projeto = models.CharField(max_length=250, blank=True, null=True)
    especificacoes_tecnicas = models.CharField(max_length=250, blank=True, null=True)
    orcamentos_detalhados = models.CharField(max_length=250, blank=True, null=True)
    composicoes_custos_unitarios = models.CharField(max_length=250, blank=True, null=True)
    detalhamento_bdi = models.CharField(max_length=250, blank=True, null=True)
    cronograma_fisico_financeiro_empreendimento = models.CharField(max_length=250, blank=True, null=True)
    memoria_calculo_dimensionamento = models.CharField(max_length=250, blank=True, null=True)
    declaracao_bem_uso_comum_povo = models.CharField(max_length=250, blank=True, null=True)
    art_projeto = models.CharField(max_length=250, blank=True, null=True)
    art_orcamento = models.CharField(max_length=250, blank=True, null=True)
    declaracao_munutencao_conservacao = models.CharField(max_length=250, blank=True, null=True)
    declaracao_regime_execucao_obra = models.CharField(max_length=250, blank=True, null=True)
    equipe_coordenacao_projeto = models.CharField(max_length=250, blank=True, null=True)
    contrato_elaboracao_projeto_engenharia = models.CharField(max_length=250, blank=True, null=True)

    # 4 - Providencias a serem adotadas
    servico_apto_para_analise_tecnica = models.CharField(max_length=250, blank=True, null=True)
    comentario_analise_tecnica = models.CharField(max_length=250, blank=True, null=True)
    servico_terceirizado = models.CharField(max_length=250, blank=True, null=True)
    justificativa_comentarios = models.CharField(max_length=250, blank=True, null=True)
    atividade = models.CharField(max_length=250, blank=True, null=True)
    produto = models.CharField(max_length=250, blank=True, null=True)
    linha = models.CharField(max_length=250, blank=True, null=True)
    fonte = models.CharField(max_length=250, blank=True, null=True)
    responsavel_verificacao = models.CharField(max_length=250, blank=True, null=True)
    data = models.CharField(max_length=250, blank=True, null=True)
    local_data = models.CharField(max_length=250, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=250, blank=True, null=True)
    matricula = models.CharField(max_length=250, blank=True, null=True)
    cpf = models.CharField(max_length=250, blank=True, null=True)
    crea = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'projeto de estrada'
        verbose_name_plural = 'projetos de estrada'

    def __str__(self):
        return f'Projeto de estrada Nº {self.id}'


class Equipamento(Projeto):
    # 1 - Identificação
    sr = models.CharField(max_length=250, blank=True, null=True)
    numero_contrato = models.CharField(max_length=250, blank=True, null=True)
    data_assinatura = models.CharField(max_length=250, blank=True, null=True)
    programa = models.CharField(max_length=250, blank=True, null=True)
    modalidade = models.CharField(max_length=250, blank=True, null=True)
    proponente = models.CharField(max_length=250, blank=True, null=True)
    tipo_proponente = models.CharField(max_length=250, blank=True, null=True)
    empreendimento = models.CharField(max_length=250, blank=True, null=True)
    localizacao = models.CharField(max_length=250, blank=True, null=True)

    # 2 - Objetivo
    objetivo_pleito = models.CharField(max_length=250, blank=True, null=True)

    # 3 - Documentação fornecida para a análise técnica do empreendimento
    copia_plano_trabalho = models.CharField(max_length=250, blank=True, null=True)
    qci = models.CharField(max_length=250, blank=True, null=True)
    especificacoes_detalhadas = models.CharField(max_length=250, blank=True, null=True)
    orcamentos_detalhados = models.CharField(max_length=250, blank=True, null=True)
    cotacao_mercado = models.CharField(max_length=250, blank=True, null=True)
    cronograma_fisico_financeiro_empreendimento = models.CharField(max_length=250, blank=True, null=True)
    plano_uso_equipamentos_adquiridos = models.CharField(max_length=250, blank=True, null=True)
    documento_titularidade_area = models.CharField(max_length=250, blank=True, null=True)
    art_projeto = models.CharField(max_length=250, blank=True, null=True)
    art_orcamento = models.CharField(max_length=250, blank=True, null=True)
    declaracao_munutencao_conservacao = models.CharField(max_length=250, blank=True, null=True)
    declaracao_viabilidade_forneceimento_energia = models.CharField(max_length=250, blank=True, null=True)
    declaracao_viabilidade_forneceimento_agua = models.CharField(max_length=250, blank=True, null=True)
    declaracao_aquisicao_equipamentos = models.CharField(max_length=250, blank=True, null=True)
    equipe_coordenacao_projeto = models.CharField(max_length=250, blank=True, null=True)

    # 4 - Providencias a serem adotadas
    servico_apto_para_analise_tecnica = models.CharField(max_length=250, blank=True, null=True)
    comentario_analise_tecnica = models.CharField(max_length=250, blank=True, null=True)
    servico_terceirizado = models.CharField(max_length=250, blank=True, null=True)
    justificativa_comentarios = models.CharField(max_length=250, blank=True, null=True)
    atividade = models.CharField(max_length=250, blank=True, null=True)
    produto = models.CharField(max_length=250, blank=True, null=True)
    linha = models.CharField(max_length=250, blank=True, null=True)
    fonte = models.CharField(max_length=250, blank=True, null=True)
    responsavel_verificacao = models.CharField(max_length=250, blank=True, null=True)
    data = models.CharField(max_length=250, blank=True, null=True)
    local_data = models.CharField(max_length=250, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=250, blank=True, null=True)
    matricula = models.CharField(max_length=250, blank=True, null=True)
    cpf = models.CharField(max_length=250, blank=True, null=True)
    crea = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'projeto de equipamento'
        verbose_name_plural = 'projetos de equipamento'

    def __str__(self):
        return f'Projeto de equipamento Nº {self.id}'


class Pavimentacao(Projeto):
    # 1 - Identificação
    sr = models.CharField(max_length=250, blank=True, null=True)
    numero_contrato = models.CharField(max_length=250, blank=True, null=True)
    data_assinatura = models.CharField(max_length=250, blank=True, null=True)
    programa = models.CharField(max_length=250, blank=True, null=True)
    modalidade = models.CharField(max_length=250, blank=True, null=True)
    proponente = models.CharField(max_length=250, blank=True, null=True)
    tipo_proponente = models.CharField(max_length=250, blank=True, null=True)
    empreendimento = models.CharField(max_length=250, blank=True, null=True)
    localizacao = models.CharField(max_length=250, blank=True, null=True)

    # 2 - Objetivo
    objetivo_pleito = models.CharField(max_length=250, blank=True, null=True)

    # 3 - Documentação fornecida para a análise técnica do empreendimento
    copia_plano_trabalho = models.CharField(max_length=250, blank=True, null=True)
    qci = models.CharField(max_length=250, blank=True, null=True)
    planta_georreferenciada = models.CharField(max_length=250, blank=True, null=True)
    projeto_geometrico_planta_baixa = models.CharField(max_length=250, blank=True, null=True)
    projeto_geometrico_perfil_longitudinal = models.CharField(max_length=250, blank=True, null=True)
    projeto_terraplenagem_notas_servico = models.CharField(max_length=250, blank=True, null=True)
    projeto_terraplenagem_relatorio_volumes = models.CharField(max_length=250, blank=True, null=True)
    projeto_terraplenagem_secoes_transversais = models.CharField(max_length=250, blank=True, null=True)
    projeto_pavimentacao_secao_tipo = models.CharField(max_length=250, blank=True, null=True)
    projeto_drenagem = models.CharField(max_length=250, blank=True, null=True)
    projeto_sinalizacao_viaria = models.CharField(max_length=250, blank=True, null=True)
    projeto_calcadas_acessibilidade = models.CharField(max_length=250, blank=True, null=True)
    memorial_descritivo_projeto = models.CharField(max_length=250, blank=True, null=True)
    especificacoes_tecnicas = models.CharField(max_length=250, blank=True, null=True)
    orcamentos_detalhados = models.CharField(max_length=250, blank=True, null=True)
    composicoes_custos_unitarios = models.CharField(max_length=250, blank=True, null=True)
    detalhamento_bdi = models.CharField(max_length=250, blank=True, null=True)
    cronograma_fisico_financeiro_empreendimento = models.CharField(max_length=250, blank=True, null=True)
    memoria_calculo_dimensionamento = models.CharField(max_length=250, blank=True, null=True)
    declaracao_bem_uso_comum_povo = models.CharField(max_length=250, blank=True, null=True)
    art_projeto = models.CharField(max_length=250, blank=True, null=True)
    art_orcamento = models.CharField(max_length=250, blank=True, null=True)
    art_acessibilidade = models.CharField(max_length=250, blank=True, null=True)
    declaracao_munutencao_conservacao = models.CharField(max_length=250, blank=True, null=True)
    declaracao_existencia_rede_abastecimento_agua = models.CharField(max_length=250, blank=True, null=True)
    declaracao_existencia_solucao_esgotamento_sanitario = models.CharField(max_length=250, blank=True, null=True)
    declaracao_regime_execucao_obra = models.CharField(max_length=250, blank=True, null=True)
    equipe_coordenacao_projeto = models.CharField(max_length=250, blank=True, null=True)
    contrato_elaboracao_projeto_engenharia = models.CharField(max_length=250, blank=True, null=True)
    declaracao_autor_projeto_sinalizacao = models.CharField(max_length=250, blank=True, null=True)
    relatorio_fotografico = models.CharField(max_length=250, blank=True, null=True)

    # 4 - Providencias a serem adotadas
    servico_apto_para_analise_tecnica = models.CharField(max_length=250, blank=True, null=True)
    comentario_analise_tecnica = models.CharField(max_length=250, blank=True, null=True)
    servico_terceirizado = models.CharField(max_length=250, blank=True, null=True)
    justificativa_comentarios = models.CharField(max_length=250, blank=True, null=True)
    atividade = models.CharField(max_length=250, blank=True, null=True)
    produto = models.CharField(max_length=250, blank=True, null=True)
    linha = models.CharField(max_length=250, blank=True, null=True)
    fonte = models.CharField(max_length=250, blank=True, null=True)
    responsavel_verificacao = models.CharField(max_length=250, blank=True, null=True)
    data = models.CharField(max_length=250, blank=True, null=True)
    local_data = models.CharField(max_length=250, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=250, blank=True, null=True)
    matricula = models.CharField(max_length=250, blank=True, null=True)
    cpf = models.CharField(max_length=250, blank=True, null=True)
    crea = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'projeto de pavimentação'
        verbose_name_plural = 'projetos de pavimentação'

    def __str__(self):
        return f'Projeto de pavimentação Nº {self.id}'

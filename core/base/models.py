from decimal import Decimal

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from ordered_model.models import OrderedModelBase
from rest_framework.authtoken.models import Token


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
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)


class Prefeitura(Cliente):
    # campo do tipo imagem, com o modelo de papel timbrado da prefeitura
    timbre = models.ImageField(upload_to='uploads/%Y/%m/%d', max_length=150, blank=True, null=True)

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
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = 'profissional'
        verbose_name_plural = 'profissionais'

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = _('cargo')
        verbose_name_plural = _('cargos')

    def __str__(self):
        return self.descricao


class Prefeito(Profissional):

    class Meta:
        verbose_name = _('prefeito')
        verbose_name_plural = _('prefeitos')


class Responsavel(Profissional):

    class Meta:
        verbose_name = _('responsável')
        verbose_name_plural = _('responsáveis')


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
    lei_complementar = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateField(_('Data'), blank=False, null=False)
    data_prevista = models.DateField(_('Data Prevista'), blank=False, null=False)
    valor_contrapartida = models.DecimalField(
        _('Valor da contrapartida'), max_digits=19, default=Decimal('0.00'), decimal_places=2, blank=False, null=False)
    valor_convenio = models.DecimalField(
        _('Valor do convênio'), max_digits=19, default=Decimal('0.00'), decimal_places=2, blank=True, null=True)
    valor_repasse = models.DecimalField(
        _('Valor do repasse'), max_digits=19, default=Decimal('0.00'), decimal_places=2, blank=True, null=True)
    valor_liberado = models.DecimalField(
        _('Valor liberado'), max_digits=19, default=Decimal('0.00'), decimal_places=2, blank=True, null=True)
    objeto = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(_('Número da proposta'), max_length=150, blank=False, null=False)
    situacao = models.CharField(
        max_length=15, choices=SituacaoChoice.choices, default=SituacaoChoice.EM_ANALISE, blank=True, null=True
    )
    extrato = models.FileField(upload_to='uploads/extrato/%Y/%m/%d', max_length=150, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)
    status = models.BooleanField(default=True)

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

    def verifica_valor_liberar(self):
        return self.valor_repasse - self.valor_liberado


class Convenio(models.Model):

    class SituacaoChoice(models.TextChoices):
        AGUARDANDO_APROVACAO_PROJETO = 'aguardando-aprovacao', _('Aguardando aprovação do projeto')
        PROJETO_APROVADO = 'projeto-aprovado', _('Projeto aprovado, aguardando licitação')
        AGUARDANDO_ACEITE_LICITACAO = 'aguardando-aceite-licitacao', _('Aguardando aceite da licitação')
        LICITACAO_APROVADA = 'licitacao-aprovada', _('Licitação aprovada, aguardando recurso')
        RECURSO_EM_CONTA = 'recurso-em-conta', _('Recurso em conta, em execução')
        CONVENIO_CONCLUIDO = 'convenio-concluido', _('Convenio concluído')
        PRESTACAO_DE_CONTAS_CONCLUIDA = 'prestacao-de-contas-concluida', _('Prestação de contas concluída')

    proposta = models.ForeignKey('Proposta', on_delete=models.CASCADE, blank=True, null=True)
    orgao = models.ForeignKey('Orgao', on_delete=models.CASCADE, blank=True, null=True)
    arquivo_extrato = models.FileField(upload_to='uploads/%Y/%m/%d', max_length=150, blank=True, null=True)
    numero = models.CharField(_('Número convênio (SICONV)'), max_length=150, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)
    # data_criacao = models.DateTimeField(_('Data de Criação'), auto_now=True, blank=False, null=False)
    data_suspensiva = models.DateField(_('Data de Cláusula Suspensiva'), blank=True, null=True)
    data_vigencia = models.DateField(_('Data da Vigência'), blank=True, null=True)
    tecnico_orgao = models.ForeignKey('TecnicoOrgao', on_delete=models.CASCADE, blank=True, null=True)

    banco = models.CharField(max_length=200, blank=True, null=True)
    agencia = models.CharField(max_length=50, blank=True, null=True)
    conta = models.CharField(max_length=50, blank=True, null=True)

    data_aprovacao_projeto = models.DateField(_('Data Aprovação de Projeto'), blank=True, null=True)
    data_licitacao_projeto = models.DateField(_('Data Licitação de Projeto'), blank=True, null=True)
    data_analise_licitacao = models.DateField(_('Data Análise de Licitação'), blank=True, null=True)
    data_aceite_licitacao = models.DateField(_('Data Aceite de Licitação'), blank=True, null=True)
    data_liberacao_recurso = models.DateField(_('Data Liberação do Recurso'), blank=True, null=True)
    valor_recurso = models.DecimalField(
        _('Valor do recurso'), max_digits=19, default=Decimal('0.00'), decimal_places=2, blank=True, null=True)
    data_conclusao = models.DateField(_('Data Conclusão'), blank=True, null=True)
    data_prestacao_contas = models.DateField(_('Data Conclusão'), blank=True, null=True)

    nome_empresa_contratada = models.CharField(_('Empresa contratada'), max_length=250, blank=True, null=True)
    cnpj_empresa_contratada = models.CharField(_('CNPJ empresa contratada'), max_length=20, blank=True, null=True)
    numero_contrato = models.CharField(_('Número contrato'), max_length=150, blank=True, null=True)
    data_contrato = models.DateField(_('Data contrato'), max_length=150, blank=True, null=True)
    vigencia_contrato = models.DateField(_('Vigência contrato'), max_length=150, blank=True, null=True)
    valor_contrato = models.DecimalField(
        _('Valor contrato'), max_digits=19, default=Decimal('0.00'), decimal_places=2, blank=True, null=True)

    situacao = models.CharField(
        max_length=50,
        choices=SituacaoChoice.choices,
        default=SituacaoChoice.AGUARDANDO_APROVACAO_PROJETO,
        blank=True,
        null=True
    )
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('convênio')
        verbose_name_plural = _('convênios')

    def __str__(self):
        return f'{self.proposta}'


class ExecucaoConvenente(models.Model):
    convenio = models.ForeignKey(
        'Convenio',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    parcela = models.IntegerField(
        _('Parcela'),
        blank=False,
        null=False
    )
    data_pagamento = models.DateField(
        _('Data pagamento'),
        blank=False,
        null=False
    )
    valor_pagamento = models.DecimalField(
        _('Valor pagamento'),
        max_digits=19,
        default=Decimal('0.00'),
        decimal_places=2,
        blank=False,
        null=False
    )

    @property
    def percentual(self):
        return (self.valor_pagamento / self.convenio.valor_contrato) * 100 if self.convenio.valor_contrato > 0 else 0


class ExecucaoConcedente(models.Model):
    convenio = models.ForeignKey(
        'Convenio',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    parcela = models.IntegerField(
        _('Parcela'),
        blank=False,
        null=False
    )
    data_liberacao = models.DateField(
        _('Data liberação'),
        blank=False,
        null=False
    )
    valor_pagamento = models.DecimalField(
        _('Valor pagamento'),
        max_digits=19,
        default=Decimal('0.00'),
        decimal_places=2,
        blank=False,
        null=False
    )

    @property
    def percentual(self):
        return (self.valor_pagamento / self.convenio.proposta.valor_repasse) * 100


class Servico(models.Model):
    prefeitura = models.ForeignKey('Prefeitura', on_delete=models.CASCADE, blank=True, null=True)
    objeto = models.CharField(max_length=150, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    responsavel = models.ForeignKey('Responsavel', on_delete=models.CASCADE, blank=True, null=True)
    data_cadastro = models.DateField(_('Data de Cadastro'), auto_now=True, blank=False, null=False)
    data_prevista = models.DateField(_('Data Prevista'), blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('serviço')
        verbose_name_plural = _('serviços')

    def __str__(self):
        return f'{self.objeto}'


class Orgao(models.Model):
    descricao = models.CharField(max_length=250, blank=False, null=False)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = _('orgão')
        verbose_name_plural = _('orgãos')

    def __str__(self):
        return f'{self.descricao}'


class TecnicoOrgao(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _('técnico orgão')
        verbose_name_plural = _('técnicos orgãos')

    def __str__(self):
        return f'{self.nome}'


class Projeto(models.Model):
    class TipoChoice(models.TextChoices):
        ESTRADA = 'estrada', _('Estrada')
        EQUIPAMENTO = 'equipamento', _('Equipamento')
        PRACA = 'praca', _('Praça')
        PAVIMENTACAO = 'pavimentacao', _('Pavimentação')
        CENTRO_ESPORTIVO = 'centro_esportivo', _('Centro Esportivo')
        EDIFICACAO = 'edificacao', _('Edificação')
        OUTROS = 'outros', _('Outros')

    tipo = models.CharField(
        max_length=150, choices=TipoChoice.choices, default=None, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    def __str__(self):
        return f'{self.get_tipo_display()}'


class Item(OrderedModelBase):
    descricao = models.TextField(blank=False, null=False)
    subitem = models.ForeignKey('Item', on_delete=models.CASCADE, blank=True, null=True)
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    opcao = models.ForeignKey('Opcao', on_delete=models.CASCADE, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)
    order = models.CharField(max_length=250, blank=True, null=True)
    sort_order = models.PositiveIntegerField(editable=False, db_index=True, blank=True, null=True)
    order_field_name = "sort_order"

    class Meta:
        ordering = ("sort_order",)
        verbose_name_plural = "itens"

    def __str__(self):
        return f'{self.descricao}'


class Opcao(models.Model):
    descricao = models.BooleanField(default=False)
    alternativa = models.BooleanField(default=False)
    texto = models.BooleanField(default=False)
    responsavel = models.BooleanField(default=False)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = 'opção'
        verbose_name_plural = 'opções'

    def __str__(self):
        string = ''
        if self.descricao:
            string += f' Descrição: {self.descricao} '
        if self.alternativa:
            string += f' Alternativa: {self.alternativa} '
        if self.texto:
            string += f' Texto: {self.texto} '
        if self.responsavel:
            string += f' responsavel: {self.responsavel} '

        return string


class ItemAlternativa(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, blank=True, null=True)
    alternativa = models.ManyToManyField('Alternativa')
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    def __str__(self):
        return f'{self.item}'


class Alternativa(models.Model):
    descricao = models.CharField(max_length=250, blank=False, null=False)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    def __str__(self):
        return f'{self.descricao}'


class ProjetoControle(models.Model):
    orgao = models.ForeignKey('Orgao', on_delete=models.CASCADE, blank=True, null=True)
    convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE, blank=True, null=True)
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = 'controle'
        verbose_name_plural = 'controles'

    def __str__(self):
        string = f'{self.orgao} '
        if self.projeto:
            string += f'{self.projeto} '
        if self.convenio:
            string += f'{self.convenio} '
        return string


class ProjetoControleItem(models.Model):
    controle = models.ForeignKey('ProjetoControle', on_delete=models.CASCADE, blank=False, null=False)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, blank=True, null=True)
    alternativa = models.ForeignKey('Alternativa', on_delete=models.CASCADE, blank=True, null=True)
    responsavel = models.ForeignKey('Responsavel', on_delete=models.CASCADE, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    data_prevista = models.DateField(_('Data Prevista'), blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'itens'

    def __str__(self):
        return f'{self.item.descricao}'


class Protocolo(models.Model):
    class ResponsavelChoice(models.TextChoices):
        AGILIZA = 'agiliza', _('AGILIZA')
        FUNASA = 'funasa', _('FUNASA')
        PREFEITURA = 'prefeitura', _('PREFEITURA')
        ASSESSORIA = 'assessoria', _('ASSESSORIA')
        GABINETE_PARLAMENTAR = 'gabinete_parlamentar', _('GABINETE PARLAMENTAR')
        ORGAO_CONVENENTE = 'orgao_convenente', _('ORGAO CONVENENTE')
        CONCEDENTE = 'concedente', _('CONCEDENTE')
        OUTROS = 'outros', _('OUTROS')

    class SituacaoChoice(models.TextChoices):
        ENVIADO_ANALISE = 'enviado_analise', _('Enviado p/ análise')
        SOLICITADA_COMPLEMENTACAO = 'solicitada_complementacao', _('Solicitada complementação')
        APROVADO = 'aprovado', _('Aprovado')
        RESOLVIDO = 'resolvido', _('Resolvido')

    convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE, blank=False, null=False)
    data = models.DateField(_('Data'), auto_now=True, blank=False, null=False)
    data_protocolado = models.DateField(_('Data Protocolado'), blank=False, null=False)
    data_prevista = models.DateField(_('Data Prevista'), blank=False, null=False)
    responsavel = models.CharField(
        max_length=250, choices=ResponsavelChoice.choices, default=None, blank=True, null=True)
    consideracoes = models.TextField(blank=False, null=False)
    situacao = models.CharField(
        max_length=150, choices=SituacaoChoice.choices, default=None, blank=True, null=True)
    anexo = models.FileField(upload_to='uploads/protocolos/%Y/%m/%d', max_length=150, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)
    data_hora_criacao = models.DateTimeField(
        _('Data hora de criação'), auto_now=True, blank=False, null=True)

    def __str__(self):
        return f'{self.data} - {self.convenio}'


class Atividade(Protocolo):
    pass


class LicenciamentoAmbiental(Protocolo):
    pass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

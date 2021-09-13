from django.contrib.auth.models import User
from django.db import models
# from ordered_model.models import OrderedModelBase
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
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)


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
    lei_complementar = models.CharField(max_length=200, blank=False, null=False)
    data = models.DateField(_('Data'), blank=False, null=False)
    data_prevista = models.DateField(_('Data Prevista'), blank=False, null=False)
    valor_contrapartida = models.DecimalField(
        _('Valor da contrapartida'), max_digits=19, decimal_places=2, blank=False, null=False)
    objeto = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(_('Número da proposta'), max_length=150, blank=False, null=False)
    situacao = models.CharField(
        max_length=15, choices=SituacaoChoice.choices, default=SituacaoChoice.EM_ANALISE, blank=True, null=True
    )
    extrato = models.FileField(upload_to='uploads/extrato/%Y/%m/%d', max_length=150, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

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


class Convenio(models.Model):
    proposta = models.ForeignKey('Proposta', on_delete=models.CASCADE, blank=True, null=True)
    orgao = models.ForeignKey('Orgao', on_delete=models.CASCADE, blank=True, null=True)
    arquivo_extrato = models.FileField(upload_to='uploads/%Y/%m/%d', max_length=150, blank=True, null=True)
    numero_convenio = models.CharField(_('Número convênio (SICONV)'), max_length=150, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = _('convênio')
        verbose_name_plural = _('convênios')

    def __str__(self):
        return f'{self.proposta}'


class Orgao(models.Model):
    descricao = models.CharField(max_length=250, blank=False, null=False)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = _('orgão')
        verbose_name_plural = _('orgãos')

    def __str__(self):
        return f'{self.descricao}'


class Projeto(models.Model):
    class TipoChoice(models.TextChoices):
        ESTRADA = 'estrada', _('Estrada')
        EQUIPAMENTO = 'equipamento', _('Equipamento')
        PRACA = 'praca', _('Praca')
        PAVIMENTACAO = 'pavimentacao', _('Pavimentacao')
        CENTRO_ESPORTIVO = 'centro_esportivo', _('Centro Esportivo')
        EDIFICACAO = 'edificacao', _('Edificação')

    tipo = models.CharField(
        max_length=150, choices=TipoChoice.choices, default=None, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - {self.get_tipo_display()}'


# class Item(OrderedModelBase):
class Item(models.Model):
    descricao = models.CharField(max_length=250, blank=False, null=False)
    subitem = models.ForeignKey('Item', on_delete=models.CASCADE, blank=True, null=True)
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    opcao = models.ForeignKey('Opcao', on_delete=models.CASCADE, blank=True, null=True)
    data_criacao = models.DateField(_('Data de Criação'), auto_now=True, blank=False, null=False)
    order = models.CharField(max_length=250, blank=True, null=True)
    sort_order = models.PositiveIntegerField(editable=False, db_index=True, blank=True, null=True)
    # order_field_name = "sort_order"

    class Meta:
        # ordering = ("sort_order",)
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
        if (self.descricao):
            string += f' Descrição: {self.descricao} '
        if (self.alternativa):
            string += f' Alternativa: {self.alternativa} '
        if (self.texto):
            string += f' Texto: {self.texto} '
        if (self.responsavel):
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
        verbose_name = 'itens'

    def __str__(self):
        return f'{self.item.descricao}'


class Protocolo(models.Model):
    class ResponsavelChoice(models.TextChoices):
        AGILIZA = 'agiliza', _('AGILIZA')
        FUNASA = 'funasa', _('FUNASA')
        PREFEITURA = 'prefeitura', _('PREFEITURA')

    class SituacaoChoice(models.TextChoices):
        ENVIADO_ANALISE = 'enviado_analise', _('Enviado p/ análise')
        SOLICITADA_COMPLEMENTACAO = 'solicitada_complementacao', _('Solicitada complementação')
        APROVADO = 'aprovado', _('Aprovado')

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

    def __str__(self):
        return f'{self.data} - {self.convenio}'


class Atividade(Protocolo):
    pass


class LicenciamentoAmbiental(Protocolo):
    pass

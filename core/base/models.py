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

    prefeito = models.ForeignKey('Prefeito', models.DO_NOTHING, blank=False, null=False)
    secretario_de_obras = models.ForeignKey('SecretarioDeObras', models.DO_NOTHING, blank=True, null=True)
    secretario_financeiro = models.ForeignKey('SecretarioFinanceiro', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(_('CPF'), max_length=20, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    cargo = models.ForeignKey('Cargo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'profissional'
        verbose_name_plural = 'profissionais'

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = _('cargo')
        verbose_name_plural = _('cargos')

    def __str__(self):
        return self.nome


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
        EM_ANALISE = 'EN', _('Em análise')
        EMPENHADO = 'EP', _('Empenhado')
        APROVADO = 'AP', _('Aprovado')
        REPROVADO = 'RP', _('Reprovado')
        # SITUACAO_CHOICES = [
        #     (EM_ANALISE, 'Em análise'),
        #     (EMPENHADO, 'Empenhado'),
        #     (APROVADO, 'Aprovado'),
        #     (REPROVADO, 'Reprovado'),
        # ]
    prefeitura = models.ForeignKey('Prefeitura', models.DO_NOTHING, blank=False, null=False)
    lei_complementar = models.CharField(max_length=200, blank=False, null=False)
    data_lei = models.DateField(_('Data da lei'), blank=False, null=False)
    valor_contrapartida = models.FloatField(_('Valor da contrapartida'), blank=False, null=False)
    objeto = models.CharField(max_length=150, blank=True, null=True)
    numero_proposta = models.CharField(_('Número da proposta'), max_length=150, blank=False, null=False)
    situacao = models.CharField(max_length=2, choices=SituacaoChoice.choices, default=SituacaoChoice.EM_ANALISE, blank=True, null=True)

    class Meta:
        verbose_name = _('proposta')
        verbose_name_plural = _('propostas')

    def __str__(self):
        return f'{self.lei_complementar} {self.data_lei} - {self.numero_proposta}'

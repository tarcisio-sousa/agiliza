from django.contrib import admin
from core.base.models import Prefeitura, Prefeito, Profissional, Cargo, Proposta, Convenio, Orgao, Pavimentacao


@admin.register(Prefeitura)
class PrefeituraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'prefeito', 'secretario_obras', 'secretario_financeiro']


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    fields = ('nome', 'cargo')
    list_display = ['nome', 'cargo']


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    fields = ('descricao',)
    list_display = ['descricao', ]


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ['lei_complementar', ]


@admin.register(Prefeito)
class PrefeitoAdmin(admin.ModelAdmin):
    list_display = ['nome', ]


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ['proposta', ]


@admin.register(Orgao)
class OrgaoAdmin(admin.ModelAdmin):
    fields = ('descricao',)
    list_display = ['descricao', ]


# @admin.register(Projeto)
# class ProjetoAdmin(admin.ModelAdmin):
#     fields = ('descricao',)
#     list_display = ['descricao', ]


@admin.register(Pavimentacao)
class PavimentacaoAdmin(admin.ModelAdmin):
    # fields = ('id',)
    list_display = ['id', ]

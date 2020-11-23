from django.contrib import admin
from core.base.models import Prefeitura, Prefeito, Profissional, Cargo, Proposta


@admin.register(Prefeitura)
class PrefeituraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'prefeito', 'secretario_de_obras', 'secretario_financeiro']


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    fields = ('nome', 'cargo')
    list_display = ['nome', 'cargo']


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    fields = ('nome',)
    list_display = ['nome', ]


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ['lei_complementar', ]


@admin.register(Prefeito)
class PrefeitoAdmin(admin.ModelAdmin):
    list_display = ['nome', ]

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from core.base.models import Prefeitura, Prefeito, Profissional, Cargo, Proposta, Convenio, Orgao, Projeto, Pavimentacao


@admin.register(Prefeitura)
class PrefeituraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'prefeito', 'secretario_obras', 'secretario_financeiro']


class ProfissionalInline(admin.StackedInline):
    model = Profissional
    can_delete = False
    verbose_name_plural = 'profissional'


# @admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfissionalInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
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


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    # fields = ('descricao',)
    list_display = ['convenio', 'orgao']


@admin.register(Pavimentacao)
class PavimentacaoAdmin(admin.ModelAdmin):
    # fields = ('id',)
    list_display = ['id', ]

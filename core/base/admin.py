from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from ordered_model.admin import OrderedModelAdmin
from core.base.models import Prefeitura, Prefeito, Profissional, Cargo, Proposta, Convenio
from core.base.models import Orgao, Projeto, Item, Opcao, ItemAlternativa
from core.base.models import Responsavel, SecretarioDeObras, SecretarioFinanceiro
from core.base.models import ProjetoControle, ProjetoControleItem


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


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo']


@admin.register(SecretarioDeObras)
class SecretarioDeObrasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo']


@admin.register(SecretarioFinanceiro)
class SecretarioFinanceiroAdmin(admin.ModelAdmin):
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
    list_display = ['tipo']


# class ItemAdmin(admin.ModelAdmin):
@admin.register(Item)
class ItemAdmin(OrderedModelAdmin):
    list_display = ['descricao', 'move_up_down_links']
    # list_display = ['descricao']


# class OpcaoAdmin(OrderedModelAdmin):
@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    pass


# class ItemAlternativaAdmin(OrderedModelAdmin):
@admin.register(ItemAlternativa)
class ItemAlternativaAdmin(admin.ModelAdmin):
    list_display = ['item']


class ProjetoControleItemStacked(admin.StackedInline):
    model = ProjetoControleItem
    extra = 1


@admin.register(ProjetoControle)
class ProjetoControleAdmin(admin.ModelAdmin):
    inlines = [
        ProjetoControleItemStacked,
    ]

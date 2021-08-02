from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from ordered_model.admin import OrderedModelAdmin
from core.base.models import Prefeitura, Prefeito, Profissional, Cargo, Proposta, Convenio
from core.base.models import Orgao, Projeto, Item, Opcao, ItemAlternativa, Pavimentacao, Responsavel


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
    list_display = ['convenio', 'orgao', 'tipo']


@admin.register(Item)
class ItemAdmin(OrderedModelAdmin):
    list_display = ['descricao', 'move_up_down_links']
    # fields = ('descricao',)


@admin.register(Opcao)
class OpcaoAdmin(OrderedModelAdmin):
    pass
    # list_display = ['descricao', 'move_up_down_links']
    # fields = ('descricao',)


@admin.register(ItemAlternativa)
class ItemAlternativaAdmin(OrderedModelAdmin):
    list_display = ['item']
    # fields = ('descricao',)


@admin.register(Pavimentacao)
class PavimentacaoAdmin(admin.ModelAdmin):
    # fields = ('id',)
    list_display = ['id', ]

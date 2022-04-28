from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    path('propostas/', views.propostas, name='propostas'),
    path('proposta/', views.proposta, name='proposta'),
    path('proposta/<int:id>/', views.proposta, name='proposta'),
    path('proposta/<int:id>/<slug:situacao>/', views.proposta, name='proposta'),
    path('proposta/documento/<int:id>/', views.proposta_documento, name='proposta_documento'),
    path(
        'proposta/arquivo/extrato/<int:id>/', views.proposta_arquivo_extrato, name='proposta_arquivo_extrato'),
    path('proposta/empenhar/<int:id>/', views.proposta_empenhar, name='proposta_empenhar'),
    path('proposta/excluir/<int:id>/', views.proposta_excluir, name='proposta_excluir'),

    path('convenios/', views.convenios, name='convenios'),
    path(
        'convenio/<int:convenio_id>/projeto/controle/',
        views.convenio_projeto_controle,
        name='convenio_projeto_controle'),
    path('convenio/aprovar/projeto/<int:id>/', views.convenio_aprovar_projeto, name='convenio_aprovar_projeto'),
    path('convenio/licitar/projeto/<int:id>/', views.convenio_licitar_projeto, name='convenio_licitar_projeto'),
    path(
        'convenio/analisar/licitacao/<int:id>/',
        views.convenio_analisar_licitacao,
        name='convenio_analisar_licitacao'),
    path('convenio/aprovar/licitacao/<int:id>/', views.convenio_aprovar_licitacao, name='convenio_aprovar_licitacao'),
    path('convenio/recurso/em/conta/<int:id>/', views.convenio_recurso_conta, name='convenio_recurso_conta'),
    path('convenio/concluir/<int:id>/', views.convenio_concluir, name='convenio_concluir'),
    path(
        'convenio/concluir/prestacao/contas/<int:id>/',
        views.convenio_concluir_prestacao_contas,
        name='convenio_concluir_prestacao_contas'),
    path('convenio/excluir/<int:id>/', views.convenio_excluir, name='convenio_excluir'),
    path('arquivo/extrato/<int:id>/', views.arquivo_extrato, name='arquivo_extrato'),

    path('servicos/', views.servicos, name='servicos'),
    path('servico/', views.servico, name='servico'),
    path('servico/excluir/<int:id>/', views.servico_excluir, name='servico_excluir'),

    path('projetos/', views.projetos, name='projetos'),
    path('projeto/<int:id>/', views.projeto, name='projeto'),
    path('projeto/', views.projeto, name='projeto'),
    path('projeto/<int:id>/itens/', views.projeto_itens, name='projeto_itens'),
    path('projeto/<int:projeto_id>/item/', views.projeto_item, name='projeto_item'),
    path('projeto/<int:projeto_id>/item/<int:id>/', views.projeto_item, name='projeto_item'),
    path('projeto/<int:convenio_id>/controle/', views.projeto_controle, name='projeto_controle'),
    path('projeto/controle/<int:controle_id>/item/', views.projeto_controle_item, name='projeto_controle_item'),

    path('itens/', views.itens, name='itens'),
    path('item/<int:id>/', views.item, name='item'),
    path('item/', views.item, name='item'),
    path('opcoes/', views.opcoes, name='opcoes'),
    path('opcao/<int:id>/', views.opcao, name='opcao'),
    path('opcao/', views.opcao, name='opcao'),
    path('alternativas/', views.alternativas, name='alternativas'),
    path('alternativa/<int:id>/', views.alternativa, name='alternativa'),
    path('alternativa/', views.alternativa, name='alternativa'),
    path('itens/alternativas/', views.itens_alternativas, name='itens_alternativas'),
    path('item/alternativas/<int:id>/', views.item_alternativas, name='item_alternativas'),
    path('item/alternativas/', views.item_alternativas, name='item_alternativas'),
    path('check/list/<int:id>/', views.check_list, name='check_list'),
    path('protocolo/<int:convenio_id>/', views.protocolo, name='protocolo'),
    path('protocolos/<int:convenio_id>/', views.protocolos, name='protocolos'),
    path('protocolo/resolver/<int:id>/', views.protocolo_resolver, name='protocolo_resolver'),
    path('protocolo/excluir/<int:id>/', views.protocolo_excluir, name='protocolo_excluir'),

    path('atividades/<int:convenio_id>/', views.atividades, name='atividades'),
    path('atividade/resolver/<int:id>/', views.atividade_resolver, name='atividade_resolver'),
    path(
        'licenciamentos/ambientais/<int:convenio_id>/',
        views.licenciamentos_ambientais,
        name='licenciamentos_ambientais'),
    path('licenciamento/resolver/<int:id>/', views.licenciamento_resolver, name='licenciamento_resolver'),

    path('declaracoes/', views.declaracoes, name='declaracoes'),

]

from django.urls import path

from . import views

urlpatterns = [
    path('propostas/', views.PropostasPDFView.as_view(), name='relatorio-propostas'),
    path('convenios/', views.ConveniosPDFView.as_view(), name='relatorio-convenios'),
    path('servicos/', views.ServicosPDFView.as_view(), name='relatorio-servicos'),
    path(
        'convenio/<int:convenio_id>/projeto/controle/',
        views.ElaboracaoProjetoPDFView.as_view(), name='relatorio-convenio-projeto-controle'),
]

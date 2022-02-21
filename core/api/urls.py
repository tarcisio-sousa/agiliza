from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('propostas', views.PropostaViewSet)
router.register('convenios', views.ConvenioViewSet)
router.register('atividades', views.AtividadeViewSet)
router.register('licenciamentos/ambientais', views.LicenciamentoAmbientalViewSet)
router.register('item/controle', views.ItemControleProjetoViewSet)
router.register('tecnico/orgao', views.TecnicoOrgaoViewSet)
router.register('prefeituras', views.PrefeituraViewSet)
router.register('responsaveis', views.ResponsavelViewSet)

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('token-auth', views.AuthToken.as_view(), name='token-auth'),
]
urlpatterns += router.urls

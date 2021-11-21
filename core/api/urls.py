from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('item/controle', views.ItemControleProjetoViewSet)
router.register('tecnico/orgao', views.TecnicoOrgaoViewSet)

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
]
urlpatterns += router.urls

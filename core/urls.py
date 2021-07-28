"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView

from core.base import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    re_path('favicon.ico', favicon_view),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

    path('propostas', views.propostas, name='propostas'),
    path('propostas/<slug:filter_situacao>', views.propostas, name='propostas'),
    path('proposta', views.proposta, name='proposta'),
    path('proposta/<int:id>', views.proposta, name='proposta'),
    path('proposta/<int:id>/<slug:situacao>', views.proposta, name='proposta'),
    path('proposta/documento/<int:id>', views.proposta_documento, name='proposta_documento'),

    path('convenios', views.convenios, name='convenios'),
    path('arquivo/extrato/<int:id>', views.arquivo_extrato, name='arquivo_extrato'),

    path('projetos', views.projetos, name='projetos'),
    path('projeto/<int:id>', views.projeto, name='projeto'),
    path('projeto', views.projeto, name='projeto'),
    path('projeto/<int:id>/itens', views.projeto_itens, name='projeto_itens'),
    # # path('projeto/objeto/<int:id>', views.projeto_objeto, name='projeto_objeto'),
    # path('projeto/estrada', views.projeto_estrada, name='projeto_estrada'),
    # path('projeto/estrada/<int:id>', views.projeto_estrada, name='projeto_estrada'),
    # path('projeto/equipamento', views.projeto_equipamento, name='projeto_equipamento'),
    # path('projeto/equipamento/<int:id>', views.projeto_equipamento, name='projeto_equipamento'),
    # path('projeto/pavimentacao', views.projeto_pavimentacao, name='projeto_pavimentacao'),
    # path('projeto/pavimentacao/<int:id>', views.projeto_pavimentacao, name='projeto_pavimentacao'),
    # path('projeto/edificacao', views.projeto_edificacao, name='projeto_edificacao'),
    # path('projeto/edificacao/<int:id>', views.projeto_edificacao, name='projeto_edificacao'),
    path('itens', views.itens, name='itens'),
    path('item/<int:id>', views.item, name='item'),
    path('item', views.item, name='item'),
    path('opcoes', views.opcoes, name='opcoes'),
    path('opcao/<int:id>', views.opcao, name='opcao'),
    path('opcao', views.opcao, name='opcao'),
    path('alternativas', views.alternativas, name='alternativas'),
    path('alternativa/<int:id>', views.alternativa, name='alternativa'),
    path('alternativa', views.alternativa, name='alternativa'),
    path('itens-alternativas', views.itens_alternativas, name='itens_alternativas'),
    path('item-alternativas/<int:id>', views.item_alternativas, name='item_alternativas'),
    path('item-alternativas', views.item_alternativas, name='item_alternativas'),
    path('check-list/<int:id>', views.check_list, name='check_list'),

    path('declaracoes', views.declaracoes, name='declaracoes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administrador Agiliza - Convênios'

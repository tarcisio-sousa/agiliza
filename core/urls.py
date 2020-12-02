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
from django.urls import path

from core.base.views import home, signin, signout, propostas, proposta, proposta_documento, declaracoes, convenios, projetos, projeto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('propostas', propostas, name='propostas'),
    path('proposta', proposta, name='proposta'),
    path('proposta/<int:id>', proposta, name='proposta'),
    path('proposta/<int:id>/<slug:situacao>', proposta, name='proposta'),
    path('proposta/documento/<int:id>', proposta_documento, name='proposta_documento'),
    path('convenios', convenios, name='convenios'),
    path('projetos', projetos, name='projetos'),
    path('projeto/<int:id>', projeto, name='projeto'),
    path('declaracoes', declaracoes, name='declaracoes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administrador Agiliza - Convênios'

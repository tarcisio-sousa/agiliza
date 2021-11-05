from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('item/controle', views.item_controle_projeto_lista, name='item_controle_projeto_lista'),
    path('item/controle/<int:pk>', views.item_controle_projeto_detalhe, name='item_controle_projeto_detalhe'),
]

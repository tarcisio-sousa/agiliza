from rest_framework import serializers
from .models import ProjetoControleItem


class ItemControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetoControleItem
        fields = ['id', 'controle', 'item', 'alternativa', 'responsavel', 'observacoes', 'comentario', 'data_prevista']

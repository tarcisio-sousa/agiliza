from rest_framework import serializers
from core.base.models import ProjetoControleItem, Alternativa, Responsavel


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id', 'descricao']


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['id', 'nome']


class ItemControleSerializer(serializers.ModelSerializer):
    # alternativa = AlternativaSerializer()

    class Meta:
        model = ProjetoControleItem
        fields = ['id', 'controle', 'item', 'alternativa', 'responsavel', 'observacoes', 'comentario', 'data_prevista']


class ItemControleViewSerializer(serializers.ModelSerializer):
    alternativa = AlternativaSerializer()
    responsavel = ResponsavelSerializer()

    class Meta:
        model = ProjetoControleItem
        fields = ['id', 'controle', 'item', 'alternativa', 'responsavel', 'observacoes', 'comentario', 'data_prevista']
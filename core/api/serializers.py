from rest_framework import serializers
from core.base.models import ProjetoControleItem, Alternativa, Responsavel, TecnicoOrgao, Prefeitura


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id', 'descricao']


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['id']


class ItemControleSerializer(serializers.ModelSerializer):
    # alternativa = AlternativaSerializer()

    class Meta:
        model = ProjetoControleItem
        fields = ['id', 'controle', 'item', 'alternativa', 'responsavel', 'observacoes', 'comentario', 'data_prevista']

    def to_representation(self, item):
        ret = super().to_representation(item)
        ret['alternativa'] = AlternativaSerializer().to_representation(item.alternativa)
        ret['responsavel'] = ResponsavelSerializer().to_representation(item.responsavel)
        return ret


class TecnicoOrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicoOrgao
        fields = ['id', 'nome', 'telefone']


class PrefeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefeitura
        fields = ['id', 'nome']

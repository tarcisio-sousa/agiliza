from rest_framework import serializers
from core.base.models import ProjetoControleItem, Alternativa, TecnicoOrgao, Prefeitura, Profissional


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id', 'descricao']


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['id', 'nome']


class ItemControleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjetoControleItem
        fields = ['id', 'controle', 'item', 'alternativa', 'responsavel', 'observacoes', 'comentario', 'data_prevista']

    def to_representation(self, item):
        ret = super().to_representation(item)
        ret['alternativa'] = AlternativaSerializer().to_representation(item.alternativa)
        print(item.responsavel)
        print(ResponsavelSerializer().to_representation(item.responsavel))
        # ret['responsavel'] = ResponsavelSerializer().to_representation(item.responsavel)
        return ret


class TecnicoOrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicoOrgao
        fields = ['id', 'nome', 'telefone']


class PrefeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefeitura
        fields = ['id', 'nome']

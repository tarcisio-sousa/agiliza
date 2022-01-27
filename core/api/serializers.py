from rest_framework import serializers
from core.base.models import Proposta, Convenio, ProjetoControleItem, Alternativa
from core.base.models import TecnicoOrgao, Prefeitura, Profissional


class PropostaSerializer(serializers.ModelSerializer):
    situacao = serializers.CharField(
        source='get_situacao_display'
    )

    class Meta:
        model = Proposta
        fields = ['data', 'data_prevista', 'objeto', 'valor_convenio', 'numero', 'situacao', 'prefeitura']

    def to_representation(self, item):
        ret = super().to_representation(item)
        if item.prefeitura:
            ret['prefeitura'] = PrefeituraSerializer().to_representation(item.prefeitura)
        return ret


class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ['proposta', 'numero']

    def to_representation(self, item):
        ret = super().to_representation(item)
        if item.proposta:
            ret['proposta'] = PropostaSerializer().to_representation(item.proposta)
        return ret


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
        if item.alternativa:
            ret['alternativa'] = AlternativaSerializer().to_representation(item.alternativa)
        if item.responsavel:
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

from rest_framework import serializers
from core.base.models import Proposta, Convenio, ProjetoControleItem, Alternativa
from core.base.models import TecnicoOrgao, Prefeitura, Profissional, Atividade, LicenciamentoAmbiental


class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = ['data', 'data_prevista', 'lei_complementar', 'objeto', 'valor_contrapartida', 'valor_convenio', 'valor_repasse', 'numero', 'situacao', 'get_situacao_display', 'prefeitura', 'extrato']

    def to_representation(self, item):
        ret = super().to_representation(item)
        if item.prefeitura:
            ret['prefeitura'] = PrefeituraSerializer().to_representation(item.prefeitura)
        return ret


class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ['proposta', 'numero', 'orgao', 'data_suspensiva', 'data_vigencia', 'tecnico_orgao']
        depth = 2

    def to_representation(self, item):
        ret = super().to_representation(item)
        if item.proposta:
            ret['proposta'] = PropostaSerializer().to_representation(item.proposta)
        return ret


class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['data_protocolado', 'data_prevista', 'responsavel', 'consideracoes', 'situacao', 'get_situacao_display']
        depth = 2


class LicenciamentoAmbientalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenciamentoAmbiental
        fields = ['data_protocolado', 'data_prevista', 'responsavel', 'consideracoes', 'situacao', 'get_situacao_display']
        depth = 2


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

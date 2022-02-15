from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .filters import PropostaFilter, ConvenioFilter
from .serializers import PropostaSerializer, ItemControleSerializer, TecnicoOrgaoSerializer
from .serializers import ConvenioSerializer, PrefeituraSerializer, ResponsavelSerializer
from .serializers import AtividadeSerializer, LicenciamentoAmbientalSerializer
from core.base.models import Proposta, Convenio, Atividade, LicenciamentoAmbiental
from core.base.models import ProjetoControleItem, TecnicoOrgao, Prefeitura, Responsavel
from rest_framework.response import Response


class PropostaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer
    filter_class = PropostaFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['nome']
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
            prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
            queryset = queryset.filter(prefeitura=prefeitura)
        queryset = queryset.filter(status=True).order_by('-id')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ConvenioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
    filter_class = ConvenioFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
            prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
            queryset = queryset.filter(proposta__prefeitura=prefeitura)
        queryset = queryset.filter(status=True).order_by('-proposta__data')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AtividadeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    lookup_field = 'pk'


class LicenciamentoAmbientalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LicenciamentoAmbiental.objects.all()
    serializer_class = LicenciamentoAmbientalSerializer
    lookup_field = 'pk'


class ItemControleProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjetoControleItem.objects.all()
    serializer_class = ItemControleSerializer
    lookup_field = 'pk'


class TecnicoOrgaoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TecnicoOrgao.objects.all()
    serializer_class = TecnicoOrgaoSerializer


class PrefeituraViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Prefeitura.objects.all()
    serializer_class = PrefeituraSerializer


class ResponsavelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

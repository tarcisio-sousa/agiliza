from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import PropostaSerializer, ItemControleSerializer, TecnicoOrgaoSerializer
from .serializers import ConvenioSerializer, PrefeituraSerializer, ResponsavelSerializer
from core.base.models import Proposta, Convenio
from core.base.models import ProjetoControleItem, TecnicoOrgao, Prefeitura, Responsavel


class PropostaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer
    lookup_field = 'pk'


class ConvenioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
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

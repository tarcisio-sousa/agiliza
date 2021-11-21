from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemControleSerializer, TecnicoOrgaoSerializer
from core.base.models import ProjetoControleItem, TecnicoOrgao


class ItemControleProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjetoControleItem.objects.all()
    serializer_class = ItemControleSerializer
    lookup_field = 'pk'


class TecnicoOrgaoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TecnicoOrgao.objects.all()
    serializer_class = TecnicoOrgaoSerializer

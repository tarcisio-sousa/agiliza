from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemControleSerializer
from core.base.models import ProjetoControleItem


class ItemControleProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjetoControleItem.objects.all()
    serializer_class = ItemControleSerializer
    lookup_field = 'pk'

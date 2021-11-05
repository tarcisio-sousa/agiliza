from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ItemControleSerializer, ItemControleViewSerializer
from core.base.models import ProjetoControleItem


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def item_controle_projeto_lista(request):
    if request.method == 'GET':
        itens = ProjetoControleItem.objects.all()
        serializer = ItemControleSerializer(itens, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemControleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def item_controle_projeto_detalhe(request, pk):
    try:
        item = ProjetoControleItem.objects.get(pk=pk)
    except ProjetoControleItem.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemControleViewSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemControleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

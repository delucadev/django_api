from rest_framework import viewsets
from . import models
from . import serializers

class ProdutoViewset(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer


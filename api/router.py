from clientes.viewsets import ClienteViewset
from produto.viewsets import ProdutoViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClienteViewset)
router.register('produtos', ProdutoViewset)


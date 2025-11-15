from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet que permite realizar todas las operaciones CRUD
    sobre el modelo Producto utilizando los métodos proporcionados
    por ModelViewSet (list, create, retrieve, update, destroy).
    """
    queryset = Producto.objects.all().order_by('-creado')
    serializer_class = ProductoSerializer

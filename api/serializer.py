from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializador que transforma instancias de Producto a JSON
    y valida los datos recibidos desde el cliente.
    """
    class Meta:
        model = Producto
        fields = '__all__'

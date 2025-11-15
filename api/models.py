from django.db import models

class Producto(models.Model):
    """
    Modelo que representa un producto dentro de la base de datos.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Retorna el nombre del producto como representación del objeto.
        """
        return self.nombre

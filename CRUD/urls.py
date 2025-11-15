from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ProductoViewSet

# Router que genera automáticamente las rutas del CRUD
router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')

urlpatterns = [
    # Ruta del panel administrativo
    path('admin/', admin.site.urls),

    # Rutas del API generadas por el router
    path('api/', include(router.urls)),
]

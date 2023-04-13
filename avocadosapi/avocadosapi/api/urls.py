from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UsuarioViewSet, ProductoViewSet, ClienteViewSet, CrearVentaViewSet, detallesViewSet

router = routers.DefaultRouter ()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'creaventa', CrearVentaViewSet)
router.register(r'detalles', detallesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import prestamos

router = DefaultRouter()
router.register(r'prestamos', prestamos, basename='prestamos')

urlpatterns = [
    path('', include(router.urls))
]

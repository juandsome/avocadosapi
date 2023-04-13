from rest_framework import serializers
from .models import prestamo, usuario

class usuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields= [
            'first_name', 'last_name', 'id', 'email'
        ]

class prestamoSerializer (serializers.ModelSerializer):

    class Meta:
        model = prestamo
        fields = [
            'monto_prestado', 'cliente'
        ]


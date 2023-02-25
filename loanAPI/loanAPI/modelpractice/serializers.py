from rest_framework import serializers
from models import prestamo


class prestamoSerializer (serializers.ModelSerializer):
    class meta:
        model=prestamo
        fields = [
            'monto_prestado', 'usuario'
        ]
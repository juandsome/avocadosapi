from rest_framework import serializers
from .models import Usuario, Producto, Cliente,Factura, Detalle
from rest_framework.authtoken.models import Token

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'rol', 'password']
        def create (self, validate_data):
            user= Usuario(username=validate_data['username'])
            user.set_password(validate_data ['password'])
            print(user.password)
            user.save()


            Token.objects.create(user=user)
            return user
class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= ['id','nombre', 'precio', 'stock',  'foto']

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields= ['id','nombre', 'cedula', 'telefono',  'direccion']

class FacturaSerializer (serializers.ModelSerializer):
    class Meta:
        model= Factura
        fields= ['id','fecha','Cliente']

class DetalleSerializer (serializers.ModelSerializer):
    class Meta:
        model= Detalle
        fields=['id','producto', 'Precio', 'Cantidad']


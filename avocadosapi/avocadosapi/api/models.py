from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

# Create your models here.

class Usuario(AbstractUser):
    roles = (
        ('empleado', 'Empleado'),
        ('jefe', 'Jefe'),
    )
    rol = models.TextField(choices=roles, default='Empleado', blank=False)
    def save(self, *args, **kwargs):
        print (self.password)
        self.set_password(self.password)
        super().save(*args,**kwargs)


class Cliente(models.Model):
    nombre = models.TextField(max_length=30, default='nombre', blank=False)
    cedula = models.TextField(max_length=8, default='cedula', blank=False, unique=True)
    direccion = models.TextField(max_length=50, blank=False, default='direccion')
    telefono = models.TextField(max_length=15, blank=False, default='telefono')
    def __str__(self):
        return self.nombre


class Factura(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, blank=True )

    def __str__(self):
        return str(self.Cliente.nombre)+' '+ str(self.id)


class Producto(models.Model):
    nombre = models.TextField(max_length=100, default='nombre');
    precio = models.FloatField(max_length=20, default=0.00)
    stock = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.nombre


class Detalle(models.Model):
    Factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Precio = models.FloatField(max_length=20, blank=False, default=0.00)
    Cantidad= models.FloatField(default=0)
    def __str__(self):
        return self.Producto.nombre + str(self.id)

    def producto (self):
        class productserializer(serializers.ModelSerializer):
            class Meta:
                model = Producto
                fields = [ 'nombre', 'precio']
        serializer = productserializer(self.Producto, many=False)
        return serializer.data



class Historial (models.Model):
    dia= models.DateTimeField(auto_now_add=True, blank=True)
    ganancias= models.FloatField(default=0.00)
    ventas= models.IntegerField(default=0)


class Negocio():
    nombre= models.TextField(blank=True,max_length=150)


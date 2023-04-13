from django.contrib import admin
from .models import  Usuario, Cliente, Producto, Detalle, Factura
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Factura)


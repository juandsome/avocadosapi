from django.shortcuts import render
from rest_framework import  viewsets, status
from rest_framework.response import Response
from .models import Usuario, Producto, Cliente, Factura, Detalle
from .serializers import UsuarioSerializer, ProductoSerializer, ClienteSerializer, FacturaSerializer, DetalleSerializer
from rest_framework.decorators import action
from rest_framework.authentication import  TokenAuthentication

class UsuarioViewSet (viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    @action(detail=False, methods=['GET', 'POST'], url_path='ola')
    def lista (self, request):
        usuarios= Usuario.objects.all()
        serializer=UsuarioSerializer(usuarios,many=True)
        response= {'mensaje':serializer.data}
        return Response (response, status=status.HTTP_200_OK)

    @action(detail=False,  methods=['GET', 'POST'], url_path='get-user')
    def isloggedin (self,request):
        print(request.user)
        if (request.user.username ==''):
            response = {'mensaje': 'no logeado'}
            estatus = status.HTTP_400_BAD_REQUEST
        else:
            serializer = UsuarioSerializer(request.user, many=False)
            response = {'usuario': serializer.data}
            estatus = status.HTTP_200_OK

        return Response (response,status=estatus)

class ProductoViewSet (viewsets.ModelViewSet):
    queryset=Producto.objects.order_by('nombre')
    serializer_class = ProductoSerializer
    @action(detail=False,methods=['POST'])
    def delete (self,request):
        id=request.data['id']
        print (id)
        Producto.objects.get(id=id).delete()
        return Response({'mensaje': 'eliminado'}, status=status.HTTP_200_OK)
    @action(detail=False ,methods=['PUT'])
    def put (self,request):

        newproduct=Producto.objects.get(id=request.data['id'])
        newproduct.nombre=request.data['nombre']
        newproduct.stock=request.data['stock']
        newproduct.precio=request.data['precio']
        newproduct.save()
        serializer=ProductoSerializer(newproduct,many=False)

        return Response (serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'],detail=False)
    def searchproduct (self,request):
        productos=Producto.objects.filter(nombre__contains=request.GET['word'])
        serializer = ProductoSerializer(productos,many=True)
        return Response( serializer.data, status=status.HTTP_200_OK)
class ClienteViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    @action(methods=['GET'], detail=False, url_path='cliente' )
    def getClient (self,request):
        try:
            cliente= Cliente.objects.get (cedula=request.GET['cedula'])
            serializer = ClienteSerializer(cliente,many=False)
            return Response (serializer.data, status= status.HTTP_200_OK)
        except:
            return Response({'message', 'cliente no registrado'}, status=status.HTTP_200_OK)

class CrearVentaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def crearFactura (self, cliente):
        factura=Factura.objects.create(Cliente=cliente)
        return factura

    def crearDetalles(self,ProductosToFacturar,factura):
        for detailProducto in ProductosToFacturar:
            producto=Producto.objects.get(id=detailProducto['id'])
            Detalle.objects.create(Producto=producto,
                           Factura=factura,
                           Cantidad=detailProducto['cantidad'],
                            Precio=detailProducto['precio']
                            )
            producto.stock-=float(detailProducto['cantidad'])
            producto.save()

    @action(methods=['GET'], detail=False, url_path='find')
    def findFactura(self,request):
        facturas=Factura.objects.all()
        serializer=FacturaSerializer(facturas,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False, url_path='getfactura')
    def getFactura(self,request):
        id=request.GET['id']
        factura= Factura.objects.get(id=id)
        detalles=Detalle.objects.filter(Factura=factura)
        cliente=Cliente.objects.get(id=factura.Cliente.id)
        facSerializer=FacturaSerializer(factura,many=False)
        detallesSerializer = DetalleSerializer(detalles, many=True)
        clienteSerializer = ClienteSerializer(cliente, many=False)

        return Response ({'factura': facSerializer.data, 'detalles':detallesSerializer.data,'cliente': clienteSerializer.data}, status=status.HTTP_200_OK)

    @action(methods=['POST','GET'], detail=False, url_path='generarventa')
    def generarVenta (self, request):
        try:
            cliente = request.data['cliente']['id']
        except:
            cliente = 0
        cliente = Cliente.objects.get(id=cliente)
        factura= self.crearFactura(cliente)
        productos = request.data['lista']

        self.crearDetalles(productos,factura)

        return Response ({'message':'ok'}, status=status.HTTP_200_OK)

class detallesViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer



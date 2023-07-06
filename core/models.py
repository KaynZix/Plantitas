from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from distutils.command.upload import upload

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    
    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)
    
# Create your models here.

class descuento(models.Model):
    idDescuento = models.IntegerField(primary_key=True)
    nombreDescuento = models.CharField(max_length=20)
    cantidadDescuento = models.IntegerField()
    estado = models.BooleanField()
    
    def __str__(self):
        return str(self.idDescuento)+" - "+self.nombreDescuento+" ("+str(self.cantidadDescuento) +"%)"

class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=200, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen =models.ImageField(upload_to= "productos")
    oferta = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=1000, null=True)
    descuento_aplicado = models.ForeignKey(descuento, null=True, blank=True, on_delete=models.CASCADE )

    def tachado(self):
        if (self.oferta) and (self.descuento_aplicado != None):
            return int(round(self.precio / 100 * (self.descuento_aplicado.cantidadDescuento)))
        else:
            return ""
    
    def __str__(self):
        return self.codigo+" - "+self.nombre
    
class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.producto.nombre[0:10]+" "+str(self.venta.id)
    

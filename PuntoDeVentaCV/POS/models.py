from django.db import models

# Create your models here.

class Distribuidor(models.Model):
    Distribuidor=models.CharField(max_length=200)
    Correo=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=20)
    Descripcion=models.CharField(max_length=1000)
    Direccion=models.CharField(max_length=200)

class Categoria(models.Model):
    Categoria=models.CharField(max_length=200)

class Marca(models.Model):
    Marca=models.CharField(max_length=200)

class Producto(models.Model):
    Producto = models.CharField(max_length=200)
    Cantidad = models.IntegerField(default=0)
    PVenta = models.FloatField(default=0,verbose_name="Precio de Venta")
    PCompra = models.FloatField(default=0,verbose_name="Precio de Compra")
    Descripcion = models.CharField(max_length=1000)
    IdDistribuidor=models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    IdCategoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    IdMarca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    Imagen = models.ImageField(upload_to='images/', default='images/default.png')

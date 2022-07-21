from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.
class user(AbstractUser):
    ciudad=models.CharField(max_length=30,null=True,blank=True)
    direccion=models.CharField(max_length=40,null=True,blank=True)
    codLogin=models.CharField(max_length=30,null=True,blank=True)

class producto(models.Model):
    ID_producto=models.AutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=250)
    category=models.CharField(max_length=30)
    imagen=models.ImageField()
    stock=models.IntegerField()
    precio_unitario=models.IntegerField()
    calificacion=models.IntegerField()
    descuento=models.IntegerField()

class factura(models.Model):
    ID_factura=models.AutoField(primary_key=True)
    fecha=models.DateField()
    forma_pago=models.CharField(max_length=20)
    valor_compra=models.IntegerField()
    estado=models.CharField(max_length=20)
    Id_cliecte=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)

class factura_producto(models.Model):
    ID_facPro=models.AutoField(primary_key=True)
    Id_producto=models.ForeignKey(producto,null=True,blank=True,on_delete=models.CASCADE)
    Id_factura=models.ForeignKey(factura,null=True,blank=True,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=0)

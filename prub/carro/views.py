from ast import Return
from django.shortcuts import render, redirect
from database.models import producto
from carro.carro import carro as carroshop
from database.models import producto as Productos
def carrito(request):
    #car=carrito
    if request.user.is_authenticated:
        return render(request,'html/shopping_car.html')
    else:
        return redirect("tienda")

def agregar_producto(request,producto_id):
    if request.user.is_authenticated:
        car=carroshop(request)
        producto=Productos.objects.get(ID_producto=producto_id)
        car.agregar(producto)
        return render(request,'html/shopping_car.html')
    return redirect("tienda")

def restar(request,producto_id):
    car=carroshop(request)
    producto=Productos.objects.get(ID_producto=producto_id)
    car.restar(producto)
    return redirect("tienda")

def eliminar(request,producto_id):
    car=carroshop(request)
    producto=Productos.objects.get(ID_producto=producto_id)
    car.eliminar(producto)
    return redirect("tienda")


def limpiar(request):
    car=carroshop(request)
    car.limpiar
    return redirect("tienda")
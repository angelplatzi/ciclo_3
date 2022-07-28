from ast import Return
from django.shortcuts import render, redirect
from database.models import producto
from django.contrib import messages
from carro.carro import carro as carroshop
from database.models import producto as Productos


def carrito(request):
    if request.user.is_authenticated:
        return render(request,'html/shopping_car.html')
    else:
        messages.add_message(request=request,level=messages.INFO ,message="inicia sesion primero" )
        return redirect("tienda")

def agregar_producto(request,producto_id):
    if request.user.is_authenticated:
        car=carroshop(request)
        producto=Productos.objects.get(ID_producto=producto_id)
        car.agregar(producto)
        messages.add_message(request=request,level=messages.INFO ,message="producto agregado" )
        return redirect("tienda")
    messages.add_message(request=request,level=messages.INFO ,message="inicia sesion primero" )
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
    car=carroshop(request=request)
    car.limpiarcarrito()
    messages.add_message(request=request,level=messages.INFO ,message=str(car) )
    return render(request,'html/shopping_car.html')
from ast import Return
from django.shortcuts import render, redirect
from database.models import producto
from carro import carro
"""def agregar_producto(request,producto_id):
    carro=carro(request)
    producto=producto.objects.get(id=producto_id)
    carro.agregar(producto)
    Return redirect("tienda")"""
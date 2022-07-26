from django.shortcuts import render
from database.models import producto
encoding="utf-8"
# Create your views here.

def tienda(request):
    productos=producto.objects.all()
    return render(request,'tienda.html', {'productos':productos})
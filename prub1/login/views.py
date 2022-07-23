from typing_extensions import Required
from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.

def logueando(request):    
    return render(request,'plantilla/base.html') 

def salir(request):
    logout(request)
    return 
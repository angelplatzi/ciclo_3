from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.

def logueando(request):    
    return render(request,'plantilla/perfil.html') 

def salir(request):
    logout(request)
    return 
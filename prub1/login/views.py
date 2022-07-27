from pickle import FALSE, TRUE
from django.shortcuts import render
from database.admin import userAdmin
from django.contrib import admin
from django.contrib.auth import authenticate, login
from database.models import user

# Create your views here.

def logueando(request):
    return render(request,'plantilla/home.html')
    
        
    


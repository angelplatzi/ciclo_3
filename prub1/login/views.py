from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

@login_required
def logueando(request):    
    return render(request,'plantilla/perfil.html') 


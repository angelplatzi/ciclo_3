from django.shortcuts import  render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("homepage")
		messages.success(request, "regitro no exitoso" )
	form = NewUserForm()
	return render (request, "register.html")


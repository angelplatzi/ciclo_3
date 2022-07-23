from cProfile import label
from dataclasses import field, fields
import email
from email import message
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from database.models import user

# Create your forms here.
class NewUserForm(UserCreationForm):

    class Meta():
        model=user
        fields=["first_name","last_name","username","email",'password1', 'password2']
        labels={'first_name':"nombre","last_name":"apellido","username":"nombreusua","email":"correo",'password1':"cont1", 'password2':"cont2"}


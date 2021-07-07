from django import forms
from pruebaApp1.models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CrearUsuarioForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=['username','email','password1','password2']




from django import forms
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes
from django.contrib.auth.forms import UserCreationForm


class LocalForm(forms.ModelForm):

	class Meta:
		model=Local
		fields='__all__'

		widgets={
			"fecha_alta":forms.SelectDateWidget()
		}


class CustomUserCreationForm(UserCreationForm):
	pass

class UsuarioForm(forms.ModelForm):

	class Meta:
		model=Usuario
		fields='__all__'

		widgets={
			"fecha_alta":forms.SelectDateWidget()
		}


 
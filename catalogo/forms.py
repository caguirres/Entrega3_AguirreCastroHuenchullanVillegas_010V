from django import forms
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes, Perfil, Ubicacion
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


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


class UserForms(forms.ModelForm):

	class Meta:
		model=Perfil
		fields='__all__'

class UbicacionForm(ModelForm):
	class Meta:
		model = Ubicacion
		fields='__all__'

		

 
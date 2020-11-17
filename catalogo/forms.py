from django import forms
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes


class LocalForm(forms.ModelForm):

	class Meta:
		model=Local
		fields='__all__'

		widgets={
			"fecha_alta":forms.SelectDateWidget()
		}










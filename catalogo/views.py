from django.shortcuts import render
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes

# Create your views here.
def inicio(request):

	return render(
		request,
		'inicio.html',)

def galeria(request):

	return render(
		request,
		'galeria.html',)

def qs(request):

	return render(
		request,
		'qs.html',)



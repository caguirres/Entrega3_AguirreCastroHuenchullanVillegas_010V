from django.shortcuts import render
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes
from django.views import generic

# Create your views here.
def inicio(request):
	resenhas_d=Resenhas.objects.all()
	username=Resenhas.objects.all()

	return render(
		request,
		'inicio.html',
		context={'rese':resenhas_d, 'usu':username}
		)


def galeria(request):

	return render(
		request,
		'galeria.html',)

def qs(request):

	return render(
		request,
		'qs.html',)


def suscrip(request):

	return render(
		request,
		'form_suscrip.html',)








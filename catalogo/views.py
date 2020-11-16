from django.shortcuts import render
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes
from django.views import generic

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

class ResenhasListView(generic.ListView):
		model=Resenhas
		resenhas_inicio='mi_resenha'
		queryset=Resenhas.objects.filter(detalle__icontains='a')[:3]
		template_name='resenhas_list.html'






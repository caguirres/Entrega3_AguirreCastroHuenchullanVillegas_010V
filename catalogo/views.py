from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LocalForm, CustomUserCreationForm, UsuarioForm, UserForms
from django.template import RequestContext
from django.http import HttpResponse




def hello(request):
    return HttpResponse('hello')

def qs2(request):
    return HttpResponse('qs')


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
	

def agregar_local(request):

	data={

		'form':LocalForm()
	}

	if request.method =='POST':
		formulario=LocalForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"]="Guardado correctamente"
		else:
			data["form"]=formulario


	return render(request, 'local/local_add.html', data)


def listar_local(request):
	local_l=Local.objects.all()

	data={
		'local':local_l
	}

	return render(request, 'local/local_list.html', data)


def modificar_local(request, id_local):

	local = get_object_or_404(Local, id_local=id_local)

	data={
		'form':LocalForm(instance=local)
	}

	if request.method == 'POST':
		formulario=LocalForm(data=request.POST, instance=local, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			return	redirect(to="local_list")
		data["form"]=formulario
	
	return	render(request, 'local/local_mod.html', data)



def eliminar_local(request, id_local):

	local=get_object_or_404(Local, id_local=id_local)
	local.delete()
	return redirect(to="local_list")



def local_main(request):

	return render(
		request,
		'local.html',)

def registro(request):
	data={
		'form':CustomUserCreationForm()

	}
	return render(request, 'registration/registro.html', data)






#sdvfsd

class LocalCreate(CreateView):
	model=Local
	fields='__all__'

class LocalUpdate(UpdateView):
	model=Local
	fields=['id_local','nombre','direccion','correo','telefono','prom_califi','ruta_fotos','fecha_alta']

class LocalDelete(DeleteView):
	model=Local
	success_url=reverse_lazy('local')


from django.views import generic

class LocalDetailView(generic.DetailView):
	model=Local


def add_user(request):
	data = {
			'form':UserForms()
	}
	if request.method=="POST":
		perfil_form=UserForms(request.POST)
		if perfil_form.is_valid():
			perfil_form.save()
	
		else:
			data["form"]=perfil_form

	return render(
		request,
		'usuario/add_user.html',data)




def adm(request):

	return render(
		request,
		'inicio_adm.html',)


def agregar_usuario(request):

	data = {
		'form':UsuarioForm()
	}
	if request.method=='POST':
		formulario=UsuarioForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "Guardado Correctamente"
		else:
			data["form"]=formulario

	return render(
		request, 
		'Usuario/usuario_add.html', data)

def listar_usuario(request):
		lista=Usuario.objects.all()

		data={
			'usuario':lista
		}

		return render(request, 'usuario/usuario_list.html', data)


def modificar_usuario(request, id_usuario):
	usuario=get_object_or_404(Usuario, id_usuario=id_usuario)
	data = {
		'form': UsuarioForm(instance=usuario)
	}

	if request.method=='POST':
		formulario=UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='usuario_list')
		data['from'] = formulario

	return render(request,'usuario/usuario_mod.html', data )


def eliminar_usuario(request, id_usuario):
	usuario=get_object_or_404(Usuario, id_usuario=id_usuario)
	usuario.delete()
	return redirect(to="usuario_list")


def usuario_adm(request):

	return render(
		request,
		'usuario_adm.html',)

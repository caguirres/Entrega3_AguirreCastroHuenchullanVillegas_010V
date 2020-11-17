from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Usuario(models.Model):
	id_usuario=models.AutoField(primary_key=True)
	nom_usuario=models.CharField(max_length=20)
	contrasenha=models.CharField(max_length=30)
	tipo=models.CharField(max_length=1)
	estado=models.ForeignKey('Estado', on_delete=models.SET_NULL, null=True)
	fecha_alta=models.DateField(null=True, blank=True)

	def __str__(self):
		return f'{self.id_usuario}, {self.nom_usuario}, {self.tipo}, {self.estado}, {self.fecha_alta}'

class Estado(models.Model):
	id_Estado=models.AutoField(primary_key=True)
	descripcion=models.CharField(max_length=25)

	def __str__(self): 
		return self.descripcion

class Comensal(models.Model):
	id_comensal=models.AutoField(primary_key=True)
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	nombre=models.CharField(max_length=50)
	correo=models.CharField(max_length=50)
	telefono=models.CharField(max_length=12)

	def __str__(self):
		return f'{self.id_comensal},{self.usuario.nom_usuario},{self.nombre},{self.correo},{self.telefono}'

class Locatario(models.Model):
	id_locatario=models.AutoField(primary_key=True)
	Usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	nombre=models.CharField(max_length=50)
	correo=models.CharField(max_length=50)
	direc_comer=models.CharField(max_length=100)
	telef_comer=models.CharField(max_length=12)
	telefono=models.CharField(max_length=12)


	def __str__(self):
		return f'{self.id_locatario},{self.Usuario.id_usuario},{self.nombre},{self.correo},{self.direc_comer},{self.telef_comer},{self.telefono}'	

class Administrador(models.Model):
	id_admin=models.AutoField(primary_key=True)
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	nombre=models.CharField(max_length=50)
	correo=models.CharField(max_length=50)
	telefono=models.CharField(max_length=12)
	rut=models.CharField(max_length=12)

	def __str__(self):
		return f'{self.id_admin},{self.Usuario.id_usuario},{self.nombre},{self.correo},{self.telefono},{self.rut}'

class Local(models.Model):
	id_local=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=50)
	direccion=models.CharField(max_length=100)
	correo=models.CharField(max_length=50)
	telefono=models.CharField(max_length=12)
	prom_califi=models.IntegerField(default=0)
	ruta_fotos=models.CharField(max_length=100)
	fecha_alta=models.DateField(null=True, blank=True)

	def __str__(self):
		return f'{self.id_local},{self.nombre},{self.direccion},{self.correo},{self.telefono},{self.prom_califi},{self.ruta_fotos},{self.fecha_alta}'

class Menu(models.Model):
	id_menu=models.AutoField(primary_key=True)
	local=models.ForeignKey('Local', on_delete=models.SET_NULL, null=True)
	detalle=models.CharField(max_length=250)
	valor=models.IntegerField(default=0)
	fecha_alta=models.DateField(null=True, blank=True)

	def __str__(self):
		return f'{self.id_menu},{self.local.nombre},{self.detalle},{self.valor},{self.fecha_alta}'

class Calificacion(models.Model):
	id_califi=models.AutoField(primary_key=True)
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	local=models.ForeignKey('Local', on_delete=models.SET_NULL, null=True)
	valor=models.IntegerField(default=0)
	fecha_alta=models.DateField(null=True, blank=True)

	def __str__(self):
		return	f'{self.id_califi},{self.usuario.nom_usuario},{self.local.nombre},{self.valor},{self.fecha_alta}'
	
class Resenhas(models.Model):
	id_resenhas=models.AutoField(primary_key=True)
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	local=models.ForeignKey('Local', on_delete=models.SET_NULL, null=True)
	detalle=models.CharField(max_length=500)
	fecha_alta=models.DateField(null=True, blank=True)

	def __str__(self):
		return f'{self.id_resenhas},{self.usuario.nom_usuario},{self.local.nombre},{self.detalle},{self.fecha_alta}'

class Planes(models.Model):
	id_plan=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=20)
	valor=models.IntegerField(default=0)
	fecha_alta=models.DateField(null=True, blank=True)

	def __str__(self):
		return f'{self.id_plan},{self.nombre},{self.valor},{self.fecha_alta}'










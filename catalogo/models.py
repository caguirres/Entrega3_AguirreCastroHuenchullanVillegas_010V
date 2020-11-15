from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Usuario(models.Model):
	id_usuario=models.AutoField(primary_key=True)
	nom_usuario=models.CharField(max_length=20)
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

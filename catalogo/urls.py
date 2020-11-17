from django.urls import path
from . import views
from .views import agregar_local, listar_local, modificar_local, eliminar_local, local_main

urlpatterns=[
	path('',views.inicio,name='inicio'),
	path('galeria',views.galeria,name='galeria'),
	path('qs',views.qs,name='qs'),
	path('form_suscrip',views.suscrip, name='form_suscrip'),
	path('local_detalle', views.LocalDetailView.as_view(), name='local_detail'),
	path('local_add', agregar_local, name="agregar_local"),
	path('local_list', listar_local, name="local_list"),
	path('local_mod/<id_local>', modificar_local, name="local_mod"),
	path('local_del/<id_local>', eliminar_local, name="local_del"),
	path('local', views.local_main, name="local"),

]

urlpatterns+=[
	path('local_create', views.LocalCreate.as_view(), name='Local_create'),
	path('local_update', views.LocalUpdate.as_view(), name='Local_update'),
	path('local_delete', views.LocalDelete.as_view(), name='Local_delete'),

]


	



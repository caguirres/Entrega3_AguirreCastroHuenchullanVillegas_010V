from django.urls import path
from . import views

urlpatterns=[
	path('',views.inicio,name='inicio'),
	path('/templates/galeria',views.galeria,name='galeria'),
	path('/templates/qs',views.qs,name='qs'),
]

	



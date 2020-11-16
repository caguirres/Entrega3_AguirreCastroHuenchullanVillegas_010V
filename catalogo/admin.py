from django.contrib import admin
# Register your models here.
from . models import Usuario, Estado, Comensal, Locatario, Administrador, Local, Menu, Calificacion, Resenhas, Planes

admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Comensal)
admin.site.register(Locatario)
admin.site.register(Administrador)
admin.site.register(Local)
admin.site.register(Menu)
admin.site.register(Calificacion)
admin.site.register(Resenhas)
admin.site.register(Planes)

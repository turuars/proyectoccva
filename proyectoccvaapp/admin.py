from django.contrib import admin

from .models import Aplicaciones, Descargas, Home, Noticias, Socio, Usuario, CursosyCapacitaciones, Administrador, Consulta

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Socio)
admin.site.register(Home)
admin.site.register(Aplicaciones)
#admin.site.register(Descargas)
admin.site.register(Noticias)
admin.site.register(CursosyCapacitaciones)
admin.site.register(Administrador) 
admin.site.register(Consulta)








from django.contrib import admin

# Register your models here.

from .models import Curso, Comentario, Tipo

admin.site.register(Curso)
admin.site.register(Comentario)
admin.site.register(Tipo)
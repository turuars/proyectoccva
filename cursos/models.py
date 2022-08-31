from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Tipo(models.Model):
      nombre=models.CharField(max_length=100)
      created=models.DateTimeField(auto_now_add=True)
      updated=models.DateTimeField(auto_now_add=True)

      class Meta:
        verbose_name='tipo'
        verbose_name_plural='tipos'

      def __str__(self):
        return self.nombre

     

class Curso(models.Model):
      titulo=models.CharField(max_length=100)
      contenido=models.TextField()
      imagen=models.ImageField(upload_to="Cursos", null=True, blank=True)
      autor=models.ForeignKey(User, on_delete=models.CASCADE)
      categorias=models.ManyToManyField(Tipo)
      created=models.DateTimeField(auto_now_add=True)
      updated=models.DateTimeField(auto_now_add=True)

      class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'


class Comentario(models.Model):
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
     post = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='comentarios')

     class Meta:
        verbose_name='comentario'
        verbose_name_plural = 'Comentarios'

     def __str__(self):
        return self.content[:10]









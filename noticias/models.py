from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
      nombre=models.CharField(max_length=100)
      created=models.DateTimeField(auto_now_add=True)
      updated=models.DateTimeField(auto_now_add=True)

      class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

      def __str__(self):
        return self.nombre

     

class Post(models.Model):
      titulo=models.CharField(max_length=100)
      contenido=models.TextField()
      imagen=models.ImageField(upload_to="Noticias", null=True, blank=True)
      autor=models.ForeignKey(User, on_delete=models.CASCADE)
      categorias=models.ManyToManyField(Categoria)
      created=models.DateTimeField(auto_now_add=True)
      updated=models.DateTimeField(auto_now_add=True)

      class Meta:
        verbose_name='post'
        verbose_name_plural='posts'


class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.content[:10]









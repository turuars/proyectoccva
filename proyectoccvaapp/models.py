from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreYapellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    mail = models.EmailField()
    telefono = models.IntegerField()
    pais = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    
    def __str__(self):
        return self.usuario

class Socio(models.Model):
    mail = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    fecha = models.DateField()

    def __str__(self):
        return self.usuario

class Administrador(models.Model):
    mail = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    no_socio = models.BooleanField()

    def __str__(self):
        return self.usuario

class Home(models.Model):
    idSocio = models.ForeignKey(Socio,on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="home", null=True)

    def __str__(self):
        return self.usuario

class Aplicaciones(models.Model):
    idSocio = models.ForeignKey(Socio,on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="aplicaciones", null=True)

    def __str__(self):
        return self.usuario

class Descargas(models.Model):
    idSocio = models.ForeignKey(Socio,on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="descargas", null=True)

    def __str__(self):
        return self.usuario

class CursosyCapacitaciones(models.Model):
    idSocio = models.ForeignKey(Socio,on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="cursosycapacitaciones", null=True)

    def __str__(self):
        return self.usuario

class Noticias(models.Model):
    idSocio = models.ForeignKey(Socio,on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="noticias", null=True)

    def __str__(self):
        return self.usuario


class Consulta(models.Model):
    consulta = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    descripcion = models.TextField()
    nombreYapellido = models.CharField(max_length=30)
    mail = models.EmailField()
    dni = models.IntegerField()
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.usuariofrom



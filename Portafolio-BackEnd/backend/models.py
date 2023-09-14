from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Persona(AbstractUser):
    id = models.AutoField(primary_key=True)
    nombreApellido = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreApellido)


class Experiencia(models.Model):
    idExperiencia = models.AutoField(primary_key=True, max_length=2)
    posicion = models.CharField(max_length=150)
    empresa = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)
    descripcion = models.TextField()


class Educacion(models.Model):
    idEducacion = models.AutoField(primary_key=True, max_length=2)
    titulo = models.CharField(max_length=150)
    institucion = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)
    descripcion = models.TextField()


class Proyecto(models.Model):
    idProyecto = models.AutoField(primary_key=True, max_length=2)
    titulo = models.CharField(max_length=150)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)
    descripcion = models.TextField()
    url = models.TextField()


class Skill(models.Model):
    idSkill = models.AutoField(primary_key=True, max_length=2)
    tipo = models.IntegerField()
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    porcentaje = models.IntegerField()


class Investigacion(models.Model):
    idInvestigacion = models.AutoField(primary_key=True, max_length=2)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)



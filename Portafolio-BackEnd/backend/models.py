from django.db import models


# Create your models here.

class Persona(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    nombreApellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreApellido, self.usuario)


class Experiencia(models.Model):
    idExperiencia = models.CharField(primary_key=True, max_length=1)
    posicion = models.CharField(max_length=150)
    empresa = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)
    descripcion = models.TextField()


class Educacion(models.Model):
    idEducacion = models.CharField(primary_key=True, max_length=1)
    titulo = models.CharField(max_length=150)
    institucion = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)
    descripcion = models.TextField()


class Proyecto(models.Model):
    idProyecto = models.CharField(primary_key=True, max_length=1)
    titulo = models.CharField(max_length=150)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)
    descripcion = models.TextField()
    url = models.TextField()


class Skill(models.Model):
    idSkill = models.CharField(primary_key=True, max_length=1)
    tipo = models.IntegerField()
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    porcentaje = models.IntegerField()


class Investigacion(models.Model):
    idInvestigacion = models.CharField(primary_key=True, max_length=1)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)

class RedSocial(models.Model):
    idRedSocial = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='imagenes/')


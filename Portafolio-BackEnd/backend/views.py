from MySQLdb import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
import json
from Portafolio import settings

from django.views.decorators.csrf import csrf_exempt

from backend.models import Persona
from backend.models import Educacion
from backend.models import Experiencia
from backend.models import Proyecto
from backend.models import Investigacion
from backend.models import Skill


# Create your views here.

def home(request):
    personasListado = Persona.objects.get(id=1)
    listado = {'nombre': personasListado.nombreApellido, 'titulo': personasListado.titulo}
    return JsonResponse(listado, safe=False)

def sobre_mi(request):
    personasListado = Persona.objects.get(id=1)
    listado = {'nombre': personasListado.nombreApellido, 'titulo': personasListado.titulo}
    return JsonResponse(listado, safe=False)

def educacion(request):
    educacionListado = Educacion.objects.all()
    return render(request,"",{"Educacion": educacionListado})

def agregarEducacion(request):
    titulo = request.POST['titulo']
    institucion = request.POST['institucion']
    fechaInicio = request.POST['fechaInicio']
    fechaFin = request.POST['fechaFin']
    descripcion = request.POST['descripcion']
    educacion = Educacion.objects.create(titulo=titulo,institucion=institucion,fechaInicio=fechaInicio,fechaFin=fechaFin,descripcion=descripcion)
    educacion.save()
    return redirect('/')

def eliminarEducacion(request,idEducacion):
    educacion = Educacion.objects.get(idEducacion=idEducacion)
    educacion.delete()
    return redirect('/')

def experiencia(request):
    experienciaListado = Experiencia.objects.all()
    return render(request,"",{"Experiencia": experienciaListado})

def agregarExperiencia(request):
    posicion = request.POST['posicion']
    empresa = request.POST['empresa']
    fechaInicio = request.POST['fechaInicio']
    fechaFin = request.POST['fechaFin']
    descripcion = request.POST['descripcion']
    experiencia = Educacion.objects.create(posicion=posicion,empresa=empresa,fechaInicio=fechaInicio,fechaFin=fechaFin,descripcion=descripcion)
    experiencia.save()
    return redirect('/')

def eliminarExperiencia(request,idExperiencia):
    experiencia = Experiencia.objects.get(idExperiencia=idExperiencia)
    experiencia.delete()
    return redirect('/')

def proyecto(request):
    proyectoListado = Proyecto.objects.all()
    return render(request,"",{"Proyecto": proyectoListado})

def agregarProyecto(request):
    titulo = request.POST['titulo']
    fechaInicio = request.POST['fechaInicio']
    fechaFin = request.POST['fechaFin']
    descripcion = request.POST['descripcion']
    url = request.POST['url']
    proyecto = Proyecto.objects.create(titulo=titulo,fechaInicio=fechaInicio,fechaFin=fechaFin,descripcion=descripcion,url=url)
    proyecto.save()
    return redirect('/')

def eliminarProyecto(request,idProyecto):
    proyecto = Proyecto.objects.get(idProyecto=idProyecto)
    proyecto.delete()
    return redirect('/')

def investigacion(request):
    investigacionListado = Investigacion.objects.all()
    return render(request,"",{"Investigacion": investigacionListado})

def agregarInvestigacion(request):
    titulo = request.POST['titulo']
    fechaInicio = request.POST['fechaInicio']
    fechaFin = request.POST['fechaFin']
    descripcion = request.POST['descripcion']
    investigacion = Investigacion.objects.create(titulo=titulo,fechaInicio=fechaInicio,fechaFin=fechaFin,descripcion=descripcion)
    investigacion.save()
    return redirect('/')

def eliminarInvestigacion(request,idInvestigacion):
    investigacion = Investigacion.objects.get(idInvestigacion=idInvestigacion)
    investigacion.delete()
    return redirect('/')

def skill(request):
    skillListado = Skill.objects.all()
    return render(request,"",{"Skill": skillListado})

def agregarSkill(request):
    titulo = request.POST['titulo']
    tipo = request.POST['tipo']
    descripcion = request.POST['descripcion']
    porcentaje = request.POST['porcentaje']
    skill = Skill.objects.create(titulo=titulo,descripcion=descripcion,porcentaje=porcentaje,tipo=tipo)
    skill.save()
    return redirect('/')

def eliminarSkill(request,idSkill):
    skill = Skill.objects.get(idSkill=idSkill)
    skill.delete()
    return redirect('/')


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:
            # Parsea los datos JSON enviados desde Angular
            data = json.loads(request.body)

            asunto = data.get('asunto')
            mensaje = data.get('mensaje')
            email = data.get('email')
            nombre = data.get('nombre')

            template = 'Nombre: ' + nombre + '\nMensaje: ' + mensaje + '\nEmail: ' + email

            # Realiza el envío del correo electrónico
            send_mail(asunto, template, settings.EMAIL_HOST_USER, ['dayviotti2015@gmail.com'], fail_silently=False)

            return JsonResponse({'message': 'Correo electrónico enviado correctamente'})
        except Exception as e:
            return JsonResponse({'datos': e}, status=500)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return JsonResponse({'message': 'Logged in successfully'})
        else:
            return JsonResponse({'message': form.error_messages})
    return JsonResponse({'error': 'Login failed'})


def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})


from django.contrib import admin
from .models import Persona
from .models import Experiencia
from .models import Proyecto
from .models import Educacion
from .models import Skill
from .models import Investigacion

# Register your models here.

admin.site.register(Persona)
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Proyecto)
admin.site.register(Skill)
admin.site.register(Investigacion)
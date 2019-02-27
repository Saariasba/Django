from django.contrib import admin

from .models import Eleccion, Pregunta


class EleccionEnLinea(admin.StackedInline):
    model = Eleccion
    extra = 3


class PreguntaDeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Preguntas',               {'fields': ['TextoDePregunta']}),
        ('Información de Fecha', {'fields': ['FechaDePublicacion'], 'classes': ['collapse']}),
    ]
    inlines = [EleccionEnLinea,]

admin.site.register(Pregunta, PreguntaDeAdmin)
admin.site.register(Eleccion)
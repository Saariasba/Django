from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Eleccion, Pregunta


class VistaDeIndex(generic.ListView):
    NombreTemplate = 'Encuestas/index.html'
    NombreContexto = 'UltimaListaDePreguntas'

    def get_queryset(self):
        return Pregunta.objects.order_by('-FechaDePublicacion')[:5]


class VistaDeDetalles(generic.DetailView):
    Modelo = Pregunta
    NombreTemplate = 'Encuestas/detalle.html'


class VistaDeResultados(generic.DetailView):
    model = Pregunta
    NombreTemplate = 'Encuestas/resultados.html'

def Voto(Solicitud, IdPregunta):
    pregunta = get_object_or_404(Pregunta, pk=IdPregunta)
    try:
        EleccionSeleccionada = pregunta.eleccion_set.get(pk=Solicitud.POST['eleccion'])
    except (KeyError, Eleccion.DoesNotExist):
        return render(Solicitud, 'Encuestas/detalle.html', {
            'Pregunta': pregunta,
            'MensajeDeError': "No seleccionaste una elección.",
        })
    else:
        EleccionSeleccionada.votos += 1
        EleccionSeleccionada.save()
        return HttpResponseRedirect(reverse('Encuestas:resultados', args=(pregunta.id,)))
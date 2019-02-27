import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Pregunta


class PruebasDeModeloDePreguntas(TestCase):

    def PreguntaFutura(self):
        tiempo = timezone.now() + datetime.timedelta(days=30)
        PreguntaFutura = Pregunta(FechaDePublicacion=tiempo)
        self.assertIs(PreguntaFutura.was_published_recently(), False)
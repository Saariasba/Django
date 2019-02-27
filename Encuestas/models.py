from django.db import models


class Pregunta(models.Model):
    TextoDePregunta = models.CharField(max_length=200)
    FechaDePublicacion = models.DateTimeField('date published')

    def __str__(self):
        return self.TextoDePregunta


class Eleccion(models.Model):
    Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    TextoDeEleccion = models.CharField(max_length=200)
    Votos = models.IntegerField(default=0)

    def __str__(self):
        return self.TextoDeEleccion

















from django.urls import path

from . import views

app_name = 'Encuestas'
urlpatterns = [
    path('', views.VistaDeIndex.as_view(), name='index'),
    path('<int:pk>/', views.VistaDeDetalles.as_view(), name='detalles'),
    path('<int:pk>/resultados/', views.VistaDeResultados.as_view(), name='resultados'),
    path('<int:IdDePregunta>/Voto/', views.Voto, name='Voto'),
]
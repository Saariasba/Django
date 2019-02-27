from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Encuestas/', include('Encuestas.urls')),
    path('admin/', admin.site.urls),
]

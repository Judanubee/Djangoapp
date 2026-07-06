"""
URL configuration for prueba1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inicio import views #importamos para abrir views que esta en inicio
from django.conf import settings
from django.conf.urls.static import static

from registros import views as views_registros


urlpatterns = [
    path('admin/', admin.site.urls),
    path("juda/",views.nuevo, name="nuevo"),
path("contacto/", views_registros.registrar, name="contacto"),
    path("formulario/",views.formulario, name="formulario"),
    path("ejemplo/",views.ejemplo, name="ejemplo"),
    path("registrar/", views_registros.registrar, name="Registrar"),
    path('', views_registros.registros, name='principal'),
    path("comentarios/",views_registros.consultar_comentarios, name ="consultar_comentarios")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
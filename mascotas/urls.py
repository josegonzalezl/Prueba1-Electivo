from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ver_mascota, name = 'ver_mascota'),
	url(r'^nuevaMascota/$', views.Agregar_mascota, name = 'nueva_mascota'),
]
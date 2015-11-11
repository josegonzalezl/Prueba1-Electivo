from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascota

# Create your views here.

class VerMascota(ListView):
	model = Mascota
	template_name = "index.html"

ver_mascota = VerMascota.as_view()

class AgregarMascota(CreateView):
 	model = Mascota
 	template_name = "nuevaMascota.html"
 	fields = "__all__"
 	success_url = reverse_lazy("ver_mascota")

Agregar_mascota = AgregarMascota.as_view()
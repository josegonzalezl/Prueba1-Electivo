from django.contrib import admin
from .models import Mascota,MascotaPerdida,MascotaEncontrada,Foto,Usuario,CazaRecompensa

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'raza', 'sexo', 'color', 'usuario']

@admin.register(MascotaPerdida)
class MascotaPerdidaAdmin(admin.ModelAdmin):
	list_display = ['mascota', 'recompensa', 'fechaperdido', 'direccionperdido', 'comentario']
	
@admin.register(MascotaEncontrada)
class MascotaEncontradaAdmin(admin.ModelAdmin):
	list_display = ['mascota', 'recompensa', 'fechaencontrado', 'direccionencontrado', 'comentario']
	
@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
	list_display = ['mascota', 'foto']
	
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'telefono', 'mail', 'comuna', 'direccion']
	
@admin.register(CazaRecompensa)
class CazaRecompensaAdmin(admin.ModelAdmin):
	list_display = ['usuario', 'mascota_encontrada']
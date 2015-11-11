from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length = 30)
	telefono = models.CharField(max_length = 20)
	mail = models.CharField(max_length = 50)
	comuna = models.CharField(max_length = 30)
	direccion = models.CharField(max_length = 50, blank = True)
	
	class Meta:
		db_table = 'usuario'

	def __unicode__(self):
		return self.nombre

class Mascota(models.Model):
	nombre = models.CharField(max_length = 30)
	raza = models.CharField(max_length = 30)
	sexo = models.CharField(max_length = 20)
	color = models.CharField(max_length = 20)
	usuario = models.ForeignKey(Usuario, blank = True, null = True)
	
	class Meta:
		db_table = 'mascota'

	def __unicode__(self):
		return self.nombre

class MascotaPerdida(models.Model):
	mascota = models.ForeignKey(Mascota)
	recompensa = models.CharField(max_length = 20, blank = True)
	fechaperdido = models.DateTimeField(blank = False)
	direccionperdido = models.CharField(max_length = 50, blank = False)
	comentario = models.TextField()
	
	
	class Meta:
		db_table = 'mascota_perdida'

	def __unicode__(self):
		return self.mascota

class MascotaEncontrada(models.Model):
	mascota = models.ForeignKey(Mascota)
	recompensa = models.CharField(max_length = 20, blank = True)
	fechaencontrado = models.DateTimeField(blank = True)
	direccionencontrado = models.CharField(max_length = 50, blank = True)
	comentario = models.TextField()
	
	
	class Meta:
		db_table = 'mascota_econtrada'

	def __unicode__(self):
		return self.mascota
		
class Foto(models.Model):
	mascota = models.ForeignKey(Mascota)
	foto = models.CharField(max_length = 300)

	class Meta:
		db_table = 'foto_mascota'

	def __unicode__(self):
		return self.mascota


class CazaRecompensa(models.Model):
	usuario = models.ForeignKey(Usuario)
	mascota_encontrada = models.ForeignKey(MascotaEncontrada)

	class Meta:
		db_table = 'cazarecompensa'

	def __unicode__(self):
		return self.usuario


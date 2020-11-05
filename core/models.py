from django.db import models

class mensajes (models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=False , max_length=50)
    correo = models.CharField(blank=False , max_length=50)
    mensaje = models.CharField(blank=False , max_length=100)
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.nombre)
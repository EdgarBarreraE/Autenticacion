from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)

    def __str(self):
        return "PERSONA"
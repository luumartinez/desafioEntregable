from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre_apellido=models.TextField()
    edad=models.IntegerField()
    fecha_nacimiento=models.IntegerField()


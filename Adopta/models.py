from django.db import models

# Create your models here.

class gato(models.Model):
    cod_gato=models.IntegerField(primary_key=True)
    nombre_gato=models.CharField(max_length=20)
    edad_gato=models.IntegerField()
    raza_gato=models.CharField(max_length=20)
    esterelizacion_gato=models.BooleanField(True)
    fecha_nac=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.nombre_gato
from django.db import models
from datetime import datetime

# Create your models here.

class Estado(models.Model):
    des_estado = models.CharField(max_length=15)

    def __str__(self):
        return self.des_estado


class Mascota(models.Model):
    id_mas = models.AutoField(primary_key=True)
    nom_mas = models.CharField(max_length=30)
    tamano_mas = models.IntegerField(default=0)
    peso_mas = models.FloatField(default=0)
    color_mas = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    fecha_res = models.DateField('Fecha Rescate')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Regiones(models.Model):
    id_reg = models.IntegerField(primary_key=True)
    nomb_reg = models.CharField(max_length=20)

    def __str__(self):
        return self.nomb_region


class Comuna(models.Model):
    id_com = models.IntegerField(primary_key=True)
    nom_com = models.CharField(max_length=20)
    reg_com = models.ForeignKey(Regiones, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_com


class Vivienda(models.Model):
    tp_vivienda = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.tp_vivienda




class Persona(models.Model):
    rut = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=30)
    nombre = models.CharField(max_length=50)
    fec_nac = models.DateField(help_text='Fecha Nacimiento')
    fono = models.PositiveIntegerField(help_text='Numero de telefono')
    comuna = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    tp_vivienda = models.CharField(max_length=15)
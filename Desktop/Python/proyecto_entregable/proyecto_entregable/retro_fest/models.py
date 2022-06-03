from django.db import models

# Create your models here.


class Familia(models.Model):

        nombre = models.CharField(max_length=30)
        parentezco = models.CharField(max_length=30)
        edad = models.IntegerField()

class Amigos (models.Model):
        nombre = models.CharField(max_length=30)
        amigo_de = models.CharField(max_length=30)
        edad = models.IntegerField()    

class Conocidos (models.Model):
        nombre = models.CharField(max_length=30)
        conocido_de = models.CharField(max_length=30)
        edad = models.IntegerField()  
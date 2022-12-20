from django.db import models

class auto(models.Model):
 marca= models.CharField(max_length=50)
 modelo= models.CharField(max_length=50)
 km=models.BigIntegerField()

class moto(models.Model): 
 marca= models.CharField(max_length=50)
 modelo= models.CharField(max_length=50)
 km=models.BigIntegerField()

class empleado(models.Model):
    nombre= models.CharField(max_length=50)
    dni=models.BigIntegerField()

# Create your models here.

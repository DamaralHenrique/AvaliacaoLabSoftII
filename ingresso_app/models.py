from django.db import models

# Create your models here.
class Estadio(models.Model):
    nome = models.CharField(max_length=200)
    vagas = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ingresso(models.Model):
    cliente = models.CharField(max_length=200)
    vaga = models.IntegerField()
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, related_name='estadio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
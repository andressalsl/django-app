from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    cliente = models.CharField(max_length=50, blank=False)
    arquivo = models.FileField()

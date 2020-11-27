from django.db import models

class Processo(models.Model):
    pasta = models.CharField(max_length=60, blank=False)
    comarca = models.CharField(max_length=50, blank=False)
    uf = models.CharField(max_length=2, blank=False)

    def __str__(self):
        str = f"{self.pasta} - {self.comarca}-{self.uf}"
        return  str
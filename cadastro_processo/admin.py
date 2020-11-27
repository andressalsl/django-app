from django.contrib import admin
import csv,io
from .models import Cadastro
from processo.models import Processo

def upload(req):

    arq = req.FILES['file'].read().decode('UTF-8')

    for i in csv.reader(io.StringIO(arq), delimiter=';'):
        Processo.objects.get_or_create(
            pasta=i[0],
            comarca=i[1],
            uf=i[2],
        )
upload.short_description = 'Cadastrar processo'

class CadastroAdm(admin.ModelAdmin):
    list_display = ['nome', 'cliente', 'arquivo']
    ordering = ['nome']
    actions = [upload]

admin.site.register(Cadastro, CadastroAdm)

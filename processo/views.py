from django.shortcuts import render
from .models import Processo

def listar(req):
    processos = Processo.objects.all()
    return render(req, 'listar.html', {'processos': processos})
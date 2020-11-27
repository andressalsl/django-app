from django.urls import path
from .views import *

app_name = 'processo'

urlpatterns = [
    path('processos/listar/', listar, name='listar'),

]
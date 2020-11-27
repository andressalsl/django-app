from django.urls import path

from .admin import upload

app_name = 'cadastro_processo'

urlpatterns = [
    path('processo/cadastro/',upload, name='cadastro_processo'),
]
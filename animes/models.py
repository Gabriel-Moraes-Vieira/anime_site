from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Animes(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_anime = models.CharField(max_length=100)
    nomes_alternativos = models.CharField(max_length=150)
    tags_genero = models.CharField(max_length=200)
    anime_sinopse = models.TextField()
    imagem_anime = models.ImageField(upload_to='Imagens/%d/%m/%Y/', blank=True)
    links =  models.URLField(max_length=255)
    lancamentos = models.BooleanField(default=False)
    publicada = models.BooleanField(default=False)
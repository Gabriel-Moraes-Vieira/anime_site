from django.db import models
from django.contrib.auth.models import User

class Animes(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_anime = models.CharField(max_length=100)
    anime_sinopse = models.TextField()
    imagem_anime = models.ImageField(upload_to='Imagens/%d/%m/%Y/', blank=True)
    links = 
    lancamentos = models.BooleanField(default=False)
    publicada = models.BooleanField(default=False)
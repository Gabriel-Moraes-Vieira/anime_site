from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from animes.models import Animes
from django.contrib.auth import authenticate


def index(request):
    animes = Animes.objects.order_by('-data_anime').filter(publicada=True)

    animes_a_exibir = {
        'animes':animes
    }

    return render(request, 'index.html', animes_a_exibir)


def busca(request):
    return render(request, 'busca.html')

def animes(request, animes_id):
    animes = get_object_or_404(Animes, pk=animes_id)
    animes = Animes.objects.order_by('-data_anime')

    dados = {
        'animes': animes
    }

    return render(request, 'animes.html', dados)

def cria_anime(request):
    if request.method == 'POST':
        nome_anime = request.POST['nome_anime']
        nomes_alternativos = request.POST['nomes_alternativos']
        tags_genero = request.POST['tags_genero']
        anime_sinopse = request.POST['animes_sinopse']
        links = request.POST['links']
        imagem_anime = request.POST['imagem_anime']
        user = get_object_or_404(User, pk=request.user.id)
        anime = Animes.objects.create(pessoa=user ,nome_anime=nome_anime, nomes_alternativos=nomes_alternativos, tags_genero=tags_genero, anime_sinopse=anime_sinopse, links=links, imagem_anime=imagem_anime)
        print(nome_anime, nomes_alternativos, tags_genero, anime_sinopse, links, imagem_anime)
        anime.save()
        return redirect ('index')
    return render(request, 'cria_anime.html')



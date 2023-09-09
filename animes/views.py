from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from animes.models import Animes
from django.contrib.auth import authenticate
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage

def index(request):

    """ numero da pagina """
    parametro_page = request.GET.get('page','1')
    
    """ quantidade de itens por pagina """
    parametro_limit = request.GET.get('limit', '8') 

    """ se ele não for um digito e for maior do que 0, ele irá atender ao paranetro_limit como 8 itens por página """
    if not (parametro_limit.isdigit() and int(parametro_limit) > 0 ):
        parametro_limit = '8'


    animes = Animes.objects.order_by('-data_anime').filter(publicada=True)

    animes_paginacao = Paginator(animes, parametro_limit)


    """ caso o numero digitado para a página seja maior do que o número de páginas ou diferente de um número
    , seremos redirecionados para a página 1"""
    try:
        page = animes_paginacao.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = animes_paginacao.page(1)

    animes_a_exibir = {
        'quantidade_por_pagina': ['8', '16', '24', '32'],
        'animes': page
    }

    return render(request, 'index.html', animes_a_exibir)


def buscar(request):
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '7')

    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '7'

    animes_a_buscar = Animes.objects.filter(publicada=True)

    animes_a_buscar_pag = Paginator(animes_a_buscar, parametro_limit)

    try:
        page = animes_a_buscar_pag.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = animes_a_buscar_pag.page(1)
    
    
    anime_a_buscar = Animes.objects.filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        anime_a_buscar = anime_a_buscar.filter(Q(nome_anime__icontains=nome_a_buscar))
    else:
        None

        

    contexto = {
        'animes':page, 
        'animes':anime_a_buscar
    }

    return render(request, 'busca.html', contexto)

def anime(request, anime_id):
    anime = get_object_or_404(Animes, pk=anime_id)
    

    dados = {
        'anime': anime
    }

    return render(request, 'animes.html', dados)

def cria_anime(request):
    if request.method == 'POST':
        nome_anime = request.POST['nome_anime']
        nomes_alternativos = request.POST['nomes_alternativos']
        tags_genero = request.POST['tags_genero']
        anime_sinopse = request.POST['animes_sinopse']
        links = request.POST['links']
        imagem_anime = request.FILES['imagem_anime']
        user = get_object_or_404(User, pk=request.user.id)
        anime = Animes.objects.create(pessoa=user ,nome_anime=nome_anime, nomes_alternativos=nomes_alternativos, tags_genero=tags_genero, anime_sinopse=anime_sinopse, links=links, imagem_anime=imagem_anime)
        print(nome_anime, nomes_alternativos, tags_genero, anime_sinopse, links, imagem_anime)
        anime.save()
        return redirect ('index')
    return render(request, 'cria_anime.html')

def my_animes(request):
    if request.user.is_authenticated:
        id = request.user.id
        animes = Animes.objects.filter(pessoa=id)
        

    animes = {
        'animes':animes
    }

    return render(request, 'my_animes.html', animes)
    
def delete_anime(request, anime_id):
    anime_a_deletar = Animes.objects.get(pk=anime_id)
    anime_a_deletar.delete()
    return redirect('my_animes')

def conta(request, user_id):
    if request.user.is_authenticated:
        id = request.user.id

    return render(request, 'conta.html')

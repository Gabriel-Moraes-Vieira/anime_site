from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def busca(request):
    return render(request, 'busca.html')

def animes(request):
    return render(request, 'animes.html')




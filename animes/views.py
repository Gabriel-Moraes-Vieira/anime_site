from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def busca(request):
    return render(request, 'busca.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')


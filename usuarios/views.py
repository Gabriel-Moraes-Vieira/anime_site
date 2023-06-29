from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from animes.models import Animes
from django.contrib.auth import authenticate

def cadastro(request):
    if request.method == 'POST':
        email = request.POST['email']
        nome = request.POST['nome']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect ('cadastro')
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if senhas_diferentes(senha1, senha2):
            messages.error(request, 'As senhas precisam ser iguais')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já existe')
        if User.objects.filter(name=nome).exists():
            messages.error(request, 'Nome já cadastrado')
        user = User.objects.create_user(email=email, username=nome, password=senha1)
        user.save()
        messages.success(request, 'Usuario criado com sucesso')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

        

def login(request):
    return render(request, 'login.html')


def campo_vazio(campo):
    return not campo

def senhas_diferentes(senha1, senha2):
    return senha1 != senha2

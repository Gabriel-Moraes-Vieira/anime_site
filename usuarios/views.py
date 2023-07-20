from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from animes.models import Animes
from django.contrib.auth import authenticate

def cadastro(request):
    if request.method == "POST":
        email = request.POST['email']
        nome = request.POST['nome']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if campo_vazio(email):
            messages.warning(request, 'O campo email não pode ficar em branco')
            return redirect ('cadastro')
        if campo_vazio(nome):
            messages.warning(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if senhas_diferentes(senha1, senha2):
            messages.warning(request, 'As senhas precisam ser iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Este email já existe')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.warning(request, 'Nome já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(email=email, username=nome, password=senha1)
        user.save()
        print(email, nome, senha1, senha2)
        messages.success(request, 'Usuario criado com sucesso')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

        

def login(request):
    if request.method == "POST":
        nome = request.POST['nome']
        senha = request.POST['senha']
        if campo_vazio(nome):
            messages.warning(request, 'Preencha o campo email')
        if campo_vazio(senha):
            messages.warning(request, 'Preencha o campo senha')
        user = auth.authenticate(request, username=nome, password=senha)
        if user is not None:
            auth.login(request, user)
            print('usuario logado com sucesso')
            return redirect('index')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def campo_vazio(campo):
    return not campo

def senhas_diferentes(senha1, senha2):
    return senha1 != senha2

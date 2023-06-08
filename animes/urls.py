from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca', views.busca, name='busca'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro')
]
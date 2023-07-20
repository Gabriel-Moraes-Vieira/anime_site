from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca', views.busca, name='busca'),
    path('animes/<int:animes_id>', views.animes, name='animes'),
    path('cria_anime', views.cria_anime, name='cria_anime')
]
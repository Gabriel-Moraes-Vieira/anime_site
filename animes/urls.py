from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca', views.busca, name='busca'),
    path('<int:anime_id>', views.anime, name='anime'),
    path('cria_anime', views.cria_anime, name='cria_anime'),
    path('my_animes/', views.my_animes, name='my_animes')
]
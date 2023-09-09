from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('<int:anime_id>', views.anime, name='anime'),
    path('cria_anime', views.cria_anime, name='cria_anime'),
    path('my_animes/', views.my_animes, name='my_animes'),
    path('delete_anime/<int:anime_id>', views.delete_anime, name='delete_anime'),
    path('conta/<int:user_id>', views.conta, name='conta')
]
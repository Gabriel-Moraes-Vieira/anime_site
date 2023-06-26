from django.contrib import admin
from .models import Animes

class ListandoAnimes(admin.ModelAdmin):
    list_display = ('id','nome_anime','tags_genero','publicada')
    list_editable = ('publicada',)
    search_fields = ('nome_anime',)
    list_filter = ('nome_anime',)

admin.site.register(Animes, ListandoAnimes)
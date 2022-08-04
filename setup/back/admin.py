from django.contrib import admin
from back.models import Personagem, Habilidades

class Personagens(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields =  ('nome',)
    list_per_page = 10

admin.site.register(Personagem, Personagens)

class HabilidadesPersonagem(admin.ModelAdmin):
    list_display = ('id', 'personagem')
    list_display_links = ('id', 'personagem')
    search_fields =  ('personagem',)
    list_per_page = 10

admin.site.register(Habilidades, HabilidadesPersonagem)


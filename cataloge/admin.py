

from django.contrib import admin
from .models import Film, Realisateur

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('titre', 'prix_location', 'date_sortie')

@admin.register(Realisateur)
class RealisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom')    



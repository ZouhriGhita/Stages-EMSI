from django.contrib import admin
from .models import Encadrant

@admin.register(Encadrant)
class EncadrantAdmin(admin.ModelAdmin):
    list_display = ('CIN', 'nom', 'prenom', 'age', 'email', 'photo_profil', 'domaine_etude')

from django.contrib import admin
from .models import Etudiant

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('CIN', 'nom', 'prenom', 'age', 'email', 'photo_profil', 'encadrant', 'filiere')

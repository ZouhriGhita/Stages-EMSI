from django.urls import path
from . import views

urlpatterns = [
    # Lier l'URL vide de l'app à la vue liste_etudiants
    path('liste/', views.liste_etudiants, name='liste_etudiants'),
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
]
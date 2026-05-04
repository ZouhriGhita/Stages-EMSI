from django.urls import path
from . import views

urlpatterns = [
    path('mes-etudiants/', views.liste_etudiants_encadrant, name='liste_etudiants_encadrant'),
    path('fiches-suivi/', views.fiche_suivi_liste, name='fiche_suivi_liste'),
    path('absences/', views.gestion_absences, name='gestion_absences'),
]

from django.db import models


class Encadrant(models.Model):
    CIN=models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    domaine_etude = models.CharField(max_length=150)
    photo_profil = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    # La relation avec Etudiant est définie dans le modèle Etudiant via ForeignKey.
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
# Create your models here.

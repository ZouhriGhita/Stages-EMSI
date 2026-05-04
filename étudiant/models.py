from django.db import models

from encadrant.models import Encadrant


class Etudiant(models.Model):
    CIN=models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    photo_profil = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    filiere = models.CharField(max_length=150)
    encadrant = models.ForeignKey(Encadrant, on_delete=models.CASCADE, related_name="etudiants")
    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Create your models here.

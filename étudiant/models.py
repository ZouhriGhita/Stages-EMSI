from django.db import models

from encadrant.models import Encadrant

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    filiere = models.CharField(max_length=150)
    encadrant = models.ForeignKey(Encadrant, on_delete=models.CASCADE, related_name="etudiants")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Create your models here.

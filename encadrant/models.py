from django.db import models

from django.db import models

class Encadrant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialite = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Create your models here.

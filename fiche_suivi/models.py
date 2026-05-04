from django.db import models

from encadrant.models import Encadrant
from étudiant.models import Etudiant


class FicheSuivi(models.Model):
    etudiant=models.ForeignKey('étudiant.Etudiant', on_delete=models.SET_NULL, null=True)
    encadrant=models.ForeignKey('encadrant.Encadrant', on_delete=models.SET_NULL, null=True)
    cadre_stage=models.CharField(max_length=255)
    Annee_universitaire=models.CharField(max_length=20))
# Create your models here.

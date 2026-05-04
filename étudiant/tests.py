from django.test import TestCase
from .models import Etudiant

class EtudiantModelTest(TestCase):
    def test_creation_etudiant(self):
        # Tester si un objet peut être créé
        # Note: Il faudra un Encadrant ici car c'est une FK obligatoire
        pass

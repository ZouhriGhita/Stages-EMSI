from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['CIN', 'nom', 'prenom', 'age', 'email', 'filiere', 'encadrant', 'photo_profil']
        widgets = {
            'CIN': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: BK12345'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nom@exemple.com'}),
            'filiere': forms.TextInput(attrs={'class': 'form-control'}),
            'encadrant': forms.Select(attrs={'class': 'form-control'}),
            'photo_profil': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'CIN': 'Numéro de Carte d\'Identité',
            'filiere': 'Filière d\'étude',
            'encadrant': 'Encadrant assigné',
        }
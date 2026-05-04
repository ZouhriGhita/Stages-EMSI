from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Etudiant
from .forms import EtudiantForm

def liste_etudiants(request):
    # Récupérer tous les étudiants de la base de données
    etudiants = Etudiant.objects.all()
    # Envoyer les données au template
    return render(request, 'étudiant/liste.html', {'etudiants': etudiants})

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            etudiant = form.save()
            messages.success(request, f"L'étudiant {etudiant.nom} a été ajouté avec succès !")
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    
    return render(request, 'étudiant/ajouter.html', {'form': form})

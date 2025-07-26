from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Commande, LigneCommande

class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['plat', 'quantite']

# Create your views here.



@login_required
def passer_commande(request):
    if request.user.role != 'client':
        return render(request, 'erreur.html', {'message': "Seuls les clients peuvent passer commande."})

    if request.method == 'POST':
        form = LigneCommandeForm(request.POST)
        if form.is_valid():
            # Créer la commande
            commande = Commande.objects.create(client=request.user)
            ligne = form.save(commit=False)
            ligne.commande = commande
            ligne.save()
            return redirect('commande_confirmee')

    else:
        form = LigneCommandeForm()

    return render(request, 'passer_commande.html', {'form': form})


@login_required
def commande_confirmee(request):
    return render(request, 'commande_confirmee.html')

@login_required
def gestion_commandes(request):
    if request.user.role != 'serveur':
        return render(request, 'erreur.html', {'message': "Accès réservé aux serveurs."})

    commandes = Commande.objects.all().order_by('-date_commande')
    return render(request, 'gestion_commandes.html', {'commandes': commandes})



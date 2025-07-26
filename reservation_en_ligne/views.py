from django.shortcuts import render
from django import forms
from .models import Table, Reservation
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

class TableForm(forms.ModelForm):
    class Meta:
        model=Table
        fields=['numero','nombre_de_places','disponible']
        widgets = {
            'numero': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
                'min': '1',
                'placeholder': 'Numéro de la table'
            }),
            'nombre_de_places': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500',
                'min': '1',
                'placeholder': 'Nombre de places'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-green-600'
            })
        }

# Create your views here.
def ajout_table(request):
    if request.method=="POST":
        form=TableForm(request.POST)
        if form.is_valid():
            table=form.save()

    else:
        form=TableForm()

    return render(request,'ajouter_table.html',{'form':form})



def reserver(request):
    tables=Table.objects.filter(disponible=True)
    return render(request,'reservation.html',{'tables':tables})

@login_required
def confirmer_reservation(request, table_id):
    # Vérifie que l'utilisateur est bien un client
    if request.user.role != 'client':
        return render(request, 'erreur.html', {'message': "Seuls les clients peuvent réserver une table."})

    table = get_object_or_404(Table, id=table_id)

    # Vérifie si la table est disponible
    if not table.disponible:
        return render(request, 'erreur.html', {'message': "Cette table est déjà réservée."})

    # Crée la réservation
    Reservation.objects.create(client=request.user, table=table)

    # Met à jour l'état de la table
    table.disponible = False
    table.save()

    return render(request, 'reservation_confirmee.html', {'table': table})

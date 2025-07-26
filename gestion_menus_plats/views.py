from django.shortcuts import render
from .models import Plat
from django import forms
from django.db import models


class FormulairePlat(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['nom', 'description', 'prix', 'est_epuise', 'est_specialite', 'image','categorie']
        widgets = {
            'nom': forms.TextInput(  # ⚠️ Ce n'est pas une date mais un champ texte ici
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 4,
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm resize-none focus:outline-none focus:ring-2 focus:ring-blue-500'
                }
            ),
            'prix': forms.NumberInput(
                attrs={
                    'step': '0.01',
                    'min': '0',
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
                }
            ),
            'est_epuise': forms.CheckboxInput(
                attrs={
                    'class': 'form-checkbox h-5 w-5 text-blue-600'
                }
            ),
            'est_specialite': forms.CheckboxInput(
                attrs={
                    'class': 'form-checkbox h-5 w-5 text-green-600'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
                }
            ),
            'categorie': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded shadow-sm focus:ring-2 focus:ring-blue-500'
            })
        }

# Create your views here.

def ajouter_plat(request):
    if request.method=='POST':
        form=FormulairePlat(request.POST, request.FILES)
        if form.is_valid():
            plat=form.save()
    else:
        form = FormulairePlat()

    return render(request,'Ajout_plat.html',{'form': form})

def plats(request):
    plats=Plat.objects.all()

    return render(request,'plats.html',{'plats':plats})

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'role',
            'date_de_naissance',
            'password1',
            'password2',
        ]
        widgets = {
            'date_de_naissance': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
                },
                format='%Y-%m-%d'
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        self.fields['date_de_naissance'].input_formats = ['%Y-%m-%d']



User = get_user_model()

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Adresse Email",
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border rounded',
            'placeholder': 'Adresse email'
        })
    )



# Create your views here.

def connexion(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../../reservation_en_ligne/reserver')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'connexion.html', {'form': form})


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Profil')
    else:
        form = CustomUserCreationForm()

    return render(request, 'inscription.html', {'form': form})

def profil(request):
    user = request.user  # L'utilisateur actuellement connecté
    nom = user.last_name
    prenom = user.first_name
    email = user.email
    role = user.role
    date_naissance = user.date_de_naissance

    return render(request, 'Profil.html', {
        'nom': nom,
        'prenom': prenom,
        'email': email,
        'role': role,
        'date_naissance': date_naissance
    })
def connecte(request):
    return redirect('../../reservation_en_ligne/reserver')
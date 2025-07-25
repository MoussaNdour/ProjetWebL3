from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('serveur', 'Serveur'),
        ('cuisinier', 'Cuisinier'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)
    date_de_naissance = models.DateField(null=True, blank=True)
    # les champs prénom, nom, email sont déjà hérités

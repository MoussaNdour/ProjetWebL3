from django.db import models
from django.conf import settings

from gestion_menus_plats.models import Plat


class Commande(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        limit_choices_to={'role': 'client'}
    )
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[
        ('en_attente', 'En attente'),
        ('en_preparation', 'En préparation'),
        ('servie', 'Servie'),
        ('annulée', 'Annulée'),
    ], default='en_attente')

    def __str__(self):
        return f"Commande #{self.id} - Client: {self.client.username}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.plat.nom}"

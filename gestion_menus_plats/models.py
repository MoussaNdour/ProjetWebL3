from django.db import models

# Create your models here.
from django.db import models

class Plat(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    CATEGORIES = [
        ('entree', 'Entrée'),
        ('plat', 'Plat principal'),
        ('dessert', 'Dessert'),
    ]
    categorie = models.CharField(max_length=100, choices=CATEGORIES, default=CATEGORIES[0])
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=19.99)
    est_epuise = models.BooleanField(default=False)
    est_specialite = models.BooleanField(default=False)
    image=models.ImageField(upload_to='', blank=True, null=True)


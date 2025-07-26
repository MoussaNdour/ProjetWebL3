from django.db import models

# Create your models here.
from django.db import models

class Plat(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    est_epuise = models.BooleanField(default=False)
    est_specialite = models.BooleanField(default=False)


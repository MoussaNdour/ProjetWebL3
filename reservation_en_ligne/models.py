from django.conf import settings
from django.db import models

# Create your models here.

class Table(models.Model):
    numero=models.IntegerField(unique=True)
    nombre_de_places=models.IntegerField()
    disponible=models.BooleanField(default=True)


class Reservation(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'client'}
    )
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.email} - Table {self.table.numero}"



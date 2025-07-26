from django.urls import path
from . import views

urlpatterns = [
    path('passer/', views.passer_commande, name='passer_commande'),
    path('confirmee/', views.commande_confirmee, name='commande_confirmee'),
    path('gerer_commandes/', views.gestion_commandes, name='gestion_commandes'),
]
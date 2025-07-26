from django.urls import path,include
from . import views



urlpatterns=[
    path('connexion/',views.connexion,name="connexion"),
    path('inscription/',views.inscription,name="inscription"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profil/',views.profil,name="dashboard"),
    path('serveur/',views.serveur_dashboard,name="serveur_dashboard"),
    path("changer_status/<int:commande_id>",views.changer_statut_commande,name="changer_statut_commande")
]
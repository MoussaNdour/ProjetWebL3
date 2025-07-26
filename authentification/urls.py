from django.urls import path,include
from . import views



urlpatterns=[
    path('connexion/',views.connexion,name="connexion"),
    path('inscription/',views.inscription,name="inscription"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profil/',views.profil,name="dashboard")
]
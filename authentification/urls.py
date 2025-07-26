from django.urls import path,include
from . import views



urlpatterns=[
    path('connexion/',views.connexion),
    path('inscription/',views.inscription),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profil/',views.profil)
]
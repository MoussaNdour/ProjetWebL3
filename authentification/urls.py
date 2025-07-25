from django.urls import path
from . import views



urlpatterns=[
    path('connexion/',views.connexion),
    path('inscription/',views.inscription)
]
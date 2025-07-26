from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='accueil'),
    path('deconnexion',views.deconnecter,name="deconnexion")
]
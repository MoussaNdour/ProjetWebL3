from django.urls import path
from . import views


urlpatterns=[
    path('ajouter_plat/',views.ajouter_plat),
    path('plats/',views.plats,name="plats")
]


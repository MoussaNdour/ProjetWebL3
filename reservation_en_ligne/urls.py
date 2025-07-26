from django.urls import path
from . import views

urlpatterns=[
    path('reserver/',views.reserver),
    path('ajouter_table/',views.ajout_table),
    path('reserver/<int:table_id>/', views.confirmer_reservation, name='confirmer_reservation')

]
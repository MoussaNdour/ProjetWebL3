from django.urls import path
from . import views

urlpatterns=[
    path('reserver/',views.reserver,name="reserver"),
    path('ajouter_table/',views.ajout_table),
    path('reserver/<int:table_id>/', views.confirmer_reservation, name='confirmer_reservation'),
    path('gestion_reservation/',views.gestion_reservations,name="admin_dashboard"),
    path('supprimer_reservation/<int:reservation_id>',views.supprimer_reservation,name="supprimer_reservation")

]
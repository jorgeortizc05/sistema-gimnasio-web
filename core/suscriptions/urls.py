from django.contrib import admin
from django.urls import path

from core.suscriptions.views.type_suscription.views import TypeSuscriptionListView, TypeSuscriptionCreateView, \
    TypeSuscriptionUpdateView, TypeSuscriptionDeleteView
from core.suscriptions.views.client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = "suscriptions"  # Ej. suscriptions:type_suscription_list
urlpatterns = [
    #TYPE SUSCRIPCION ============================================================
    path('type-suscription/', TypeSuscriptionListView.as_view(), name="type_suscription_list"),
    path('type-suscription/create', TypeSuscriptionCreateView.as_view(), name="type_suscription_create"),
    path('type-suscription/update/<int:pk>/', TypeSuscriptionUpdateView.as_view(), name="type_suscription_update"),
    path('type-suscription/delete/<int:pk>/', TypeSuscriptionDeleteView.as_view(), name="type_suscripcion_delete"),

    #TYPE SUSCRIPCION ============================================================
    path('clients/', ClientListView.as_view(), name="client_list"),
    path('clients/create', ClientCreateView.as_view(), name="client_create"),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name="client_update"),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name="client_delete")

]

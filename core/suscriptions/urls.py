from django.contrib import admin
from django.urls import path

from core.suscriptions.views.type_suscription.views import TypeSuscriptionListView, TypeSuscriptionCreateView, \
    TypeSuscriptionUpdateView, TypeSuscriptionDeleteView

app_name = "suscriptions"  # Ej. suscriptions:type_suscription_list
urlpatterns = [
    path('type-suscription/', TypeSuscriptionListView.as_view(), name="type_suscription_list"),
    path('type-suscription/create', TypeSuscriptionCreateView.as_view(), name="type_suscription_create"),
    path('type-suscription/update/<int:pk>/', TypeSuscriptionUpdateView.as_view(), name="type_suscription_update"),
    path('type-suscription/delete/<int:pk>/', TypeSuscriptionDeleteView.as_view(), name="type_suscripcion_delete")

]

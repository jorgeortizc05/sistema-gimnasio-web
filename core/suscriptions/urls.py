from django.contrib import admin
from django.urls import path

from core.suscriptions.views.suscription.views import TypeSuscriptionListView, TypeSuscriptionCreateView

urlpatterns = [
    path('type-suscription/', TypeSuscriptionListView.as_view(), name="type_suscription_list"),
    path('type-suscription/create', TypeSuscriptionCreateView.as_view(), name="type_suscription_create"),

]
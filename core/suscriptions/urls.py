from django.contrib import admin
from django.urls import path

from core.suscriptions.views.type_person.views import *

urlpatterns = [
    path('type-person/', TypePersonListView.as_view(), name="type_people_list"),
    path('type-person/create', TypePersonCreateView.as_view(), name="type_person_create"),

]
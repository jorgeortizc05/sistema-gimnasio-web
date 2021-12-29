from django.contrib import admin
from core.suscriptions.models import TypePerson, TypeSuscription, Person, Suscription
# Register your models here.
admin.site.register(TypePerson)
admin.site.register(TypeSuscription)
admin.site.register(Person)
admin.site.register(Suscription)

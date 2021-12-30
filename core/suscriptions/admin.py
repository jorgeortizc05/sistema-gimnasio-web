from django.contrib import admin
from core.suscriptions.models import TypeSuscription, Client, Suscription, Coach

# Register your models here.
admin.site.register(TypeSuscription)
admin.site.register(Client)
admin.site.register(Suscription)
admin.site.register(Coach)

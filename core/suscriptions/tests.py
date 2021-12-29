from config.wsgi import *
from core.suscriptions.models import TypePerson, TypeSuscription
# Create your tests here.
typePeople = TypePerson.objects.all();
for tp in typePeople:
    TypePerson.objects.get(pk=tp.id).delete()
tp1 = TypePerson(name="Cliente", description="Persona que usa los servicios del sistema-gimnasio-web")
tp2 = TypePerson(name="Entrenador", description="Persona que acesora a los clientes")
tp1.save()
tp2.save()

typeSuscription = TypeSuscription.objects.all()
for ts in typeSuscription:
    TypeSuscription.objects.get(pk=ts.id).delete()

ts1 = TypeSuscription(name="Suscripcion de 1 día",num_days=1,price=1.5,description="Servicio de sistema-gimnasio-web valido por 1 día")
ts2 = TypeSuscription(name="Suscripcion de 1 semana",num_days=7,price=7,description="Servicio de sistema-gimnasio-web valido por 7 días")
ts3 = TypeSuscription(name="Suscripcion de 2 semanas",num_days=15.0,price=14,description="Servicio de sistema-gimnasio-web valido por 15 días")
ts4 = TypeSuscription(name="Suscripcion mensual",num_days=30,price=25.0,description="Servicio de sistema-gimnasio-web valido por 30 días")
ts1.save()
ts2.save()
ts3.save()
ts4.save()

typePeople = TypePerson.objects.all();
typeSuscription = TypeSuscription.objects.all()
print(typePeople)
print(typeSuscription)
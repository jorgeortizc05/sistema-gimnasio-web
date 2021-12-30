from config.wsgi import *
from core.suscriptions.models import TypeSuscription, Client

# # Create your tests here.
# ts1 = TypeSuscription(name="Suscripcion de 1 día",num_days=1,price=1.5,description="Servicio de sistema valido por 1 día")
# ts2 = TypeSuscription(name="Suscripcion de 1 semana",num_days=7,price=7,description="Servicio de sistema valido por 7 días")
# ts3 = TypeSuscription(name="Suscripcion de 2 semanas",num_days=15.0,price=14,description="Servicio de sistema valido por 15 días")
# ts4 = TypeSuscription(name="Suscripcion mensual",num_days=30,price=25.0,description="Servicio de sistema valido por 30 días")
# ts1.save()
# ts2.save()
# ts3.save()
# ts4.save()
#
# c1 = Client(first_name="Jorge", last_name="Ortiz", dni="0105182703", address="Paute", phone="0983457699")
# c1.save()

clients = Client.objects.all()
typeSuscription = TypeSuscription.objects.all()
print(typeSuscription)
print(clients)
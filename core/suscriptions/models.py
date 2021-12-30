from django.db import models

# Create your models here.
from django.forms import model_to_dict


class TypePerson(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="nombre")
    description= models.CharField(max_length=300, null=True, blank=True, verbose_name="descripción", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'Tipo Persona'
        verbose_name_plural = 'Tipos Personas'
        ordering = ['id']


class TypeSuscription(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="tipo suscripción")
    num_days = models.IntegerField(verbose_name="no. días")
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="precio")
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return f"{self.name} {self.num_days} {self.price}"

class Person(models.Model):
    first_name = models.CharField(max_length=70, verbose_name="nombres")
    last_name = models.CharField(max_length=70, verbose_name= "apellidos")
    dni = models.CharField(max_length=10, verbose_name="cedula identidad")
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name="dirección")
    email = models.CharField(max_length=150, null=True, blank=True, verbose_name="correo electrónico")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="fecha nacimiento")
    phone = models.CharField(max_length=14, null=True, blank=True, verbose_name="teléfono")
    active = models.BooleanField(default=True, verbose_name="activo");
    type_person = models.ForeignKey(TypePerson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.dni}"

class Suscription(models.Model):
    receipt_number = models.CharField(max_length=70, unique=True, verbose_name="no. recibo")
    date_suscription = models.DateTimeField(auto_created=True)
    date_from = models.DateTimeField(verbose_name="fecha desde")
    date_to = models.DateTimeField(verbose_name="fecha hasta")
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="precio")
    discount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="descuento")
    total = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="total")
    comment = models.CharField(max_length=300, null=True, blank=True, verbose_name="comentario")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    type_suscription = models.ForeignKey(TypeSuscription, on_delete=models.CASCADE)
from django.forms import *

from core.suscriptions.models import TypeSuscription


class TypeSuscriptionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = TypeSuscription
        fields = '__all__'
        #Personalizo mi atributo name, aunque eso ya hace en models verbose_name
        # labels = {
        #     'name': 'Nombre'
        # }

        widgets = {
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese el tipo de persona',
                    # 'autocomplete': 'off'
                }

            ),
            'description': Textarea(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese la descripción',
                    # 'autocomplete': 'off',
                    'cols': 3,
                    'rows': 3
                }
        )

        }

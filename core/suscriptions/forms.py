from django.forms import *

from core.suscriptions.models import TypeSuscription, Client


class TypeSuscriptionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = TypeSuscription
        fields = '__all__'
        # Personalizo mi atributo name, aunque eso ya hace en models verbose_name
        # labels = {
        #     'name': 'Nombre'
        # }

        widgets = {
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese el tipo de suscripción',
                    # 'autocomplete': 'off'
                }

            ),
            'num_days': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad de días',
                    # 'autocomplete': 'off'
                }

            ),
            'price': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese el precio',
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

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Client
        fields = '__all__'
    #     # Personalizo mi atributo name, aunque eso ya hace en models verbose_name
    #     # labels = {
    #     #     'name': 'Nombre'
    #     # }
    #
        # widgets = {
        #     'birthday': DateInput(
        #         format=('%d-%m-%Y'),
        #         attrs={
        #
        #         }
        #
        #     ),
        #     'phone': TextInput(
        #         attrs={
        #             'data-inputmask': "'mask': ['999-999-9999 [x99999]', '+099 99 99 9999[9]-9999']",
        #             'data-mask': "",
        #             'inputmode': "text"
        #         }
        #     )
        #
        # }
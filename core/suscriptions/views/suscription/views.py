from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.suscriptions.forms import ClientForm
from core.suscriptions.models import Client


# Create your views here.
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "client/create.html"
    success_url = reverse_lazy('suscriptions:client_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                # data = TypeSuscription.objects.get(pk=request.POST['id']).toJSON()
                # form = TypeSuscriptionForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna acción'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Cliente'
        context['action'] = 'create'
        context['list_url'] = reverse_lazy('suscriptions:client_list')
        return context

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "client/create.html"
    success_url = reverse_lazy('suscriptions:client_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                # data = TypeSuscription.objects.get(pk=request.POST['id']).toJSON()
                # form = TypeSuscriptionForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna acción'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición Cliente'
        context['action'] = 'update'
        context['list_url'] = reverse_lazy('suscriptions:client_list')
        return context

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/delete.html'
    success_url = reverse_lazy('suscriptions:client_list')

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Cliente'
        context['action'] = 'delete'
        context['list_url'] = reverse_lazy('suscriptions:client_list')
        return context

class ClientListView(ListView):
    model = Client
    template_name = "client/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # #Sobrescribo mi query
    # def get_queryset(self):
    #     return TypePerson.objects.filter(name__startswith="C")

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Client.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Clientes'
        context['create_url'] = reverse_lazy('suscriptions:client_create')
        return context

# #Vistas basada en funciones, no es recomendable
# def diHola(request):
#     data = {
#         'title': "Lista Tipo Personas",
#         'type_people': TypePerson.objects.all()
#     }
#     return render(request, "type_suscription/list.html", data)

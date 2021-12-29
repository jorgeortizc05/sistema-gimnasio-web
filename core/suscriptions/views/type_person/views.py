from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from core.suscriptions.forms import TypePersonForm
from core.suscriptions.models import TypePerson


# Create your views here.
class TypePersonCreateView(CreateView):
    model = TypePerson
    form_class = TypePersonForm
    template_name = "type_person/create.html"
    success_url = reverse_lazy('type_people_list')

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo tipo de persona'
        return context

class TypePersonListView(ListView):
    model = TypePerson
    template_name = "type_person/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # #Sobrescribo mi query
    # def get_queryset(self):
    #     return TypePerson.objects.filter(name__startswith="C")

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = TypePerson.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Tipo Personas'
        return context

# #Vistas basada en funciones, no es recomendable
# def diHola(request):
#     data = {
#         'title': "Lista Tipo Personas",
#         'type_people': TypePerson.objects.all()
#     }
#     return render(request, "type_person/list.html", data)

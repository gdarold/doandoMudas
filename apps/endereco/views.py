from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.endereco.models import Endereco


class EnderecoCreate(CreateView):
    model = Endereco
    fields =['cep','logradouro', 'bairro','complemento', 'cidade', 'uf' ]
    success_url = reverse_lazy('endereco_list')


class EnderecoList(ListView):
    model = Endereco


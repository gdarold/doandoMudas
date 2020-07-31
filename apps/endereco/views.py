from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.endereco.models import Endereco


class EnderecoCreate(LoginRequiredMixin, CreateView):
    model = Endereco
    fields =['cep','logradouro', 'bairro', 'numero','complemento', 'cidade', 'uf' ]


    def form_valid(self, form):
        endereco = form.save(commit = False)
        endereco.usuario = self.request.user
        endereco.save()


        return super(EnderecoCreate, self).form_valid(form)



class EnderecoList(ListView):
    model = Endereco


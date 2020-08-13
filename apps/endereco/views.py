from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.endereco.models import Endereco


class EnderecoCreate(CreateView):
    model = Endereco
    fields =['usuario','cep','logradouro', 'bairro', 'numero','complemento', 'cidade', 'uf' ]


    def form_valid(self, form):
        endereco = form.save(commit = False)
        endereco.usuario = self.request.user.pessoa
        endereco.save()


        return super(EnderecoCreate, self).form_valid(form)



class EnderecoList(ListView):
    model = Endereco


class EnderecoEdit(UpdateView):
    model = Endereco
    fields = ['usuario', 'cep', 'logradouro', 'bairro', 'numero', 'complemento', 'cidade', 'uf']


class EnderecoDelete(DeleteView):
    model = Endereco

    success_url = reverse_lazy('list_enderecos')
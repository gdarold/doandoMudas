from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.pessoa.models import Pessoa


class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['usuario', 'nome', 'sobrenome', 'cpf', 'email','celular']
    success_url = reverse_lazy('endereco')



class PessoaList(ListView):
    model = Pessoa



class PessoaEdit(UpdateView):
    model = Pessoa
    fields = ['nome', 'sobrenome', 'cpf', 'email', 'celular']




class PessoaDelete(DeleteView):
    model = Pessoa

    def get_success_url(self):
        reverse_lazy('list_pessoa')



from django.shortcuts import render

# Create your views here.



from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.doacao.models import Doacao
from apps.endereco.models import Endereco


class DoacaoCreate(CreateView):
    model = Doacao
    fields =['doador', 'tipo_doacao', 'tipo_planta','descricao', 'quantidade','peso', 'custo', 'status']


    def form_valid(self, form):
        doacao = form.save(commit = False)


        doacao.doador = self.request.user.pessoa
        usuario = doacao.doador
        print(usuario)
        endereco = Endereco.objects.filter(usuario=usuario)
        print(endereco)
        doacao.estado = "novo"
        doacao.cidade = "ss"

        doacao.save()


        return super(DoacaoCreate, self).form_valid(form)



class DoacaoList(ListView):
    model = Doacao


class DoacaoEdit(UpdateView):
    model = Doacao
    fields = ['doador', 'estado', 'cidade', 'tipo_doacao', 'tipo_planta', 'descricao',
              'quantidade', 'peso', 'custo','status']




class DoacaoDelete(DeleteView):
    model = Doacao

    success_url = reverse_lazy('list_doacoes')
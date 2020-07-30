from django.shortcuts import render

# Create your views here.


from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import AddressForm


class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('endereco:endereco')
    template_name = 'endereco/endereco2.html'
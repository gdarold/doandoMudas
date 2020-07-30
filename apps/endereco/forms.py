from django import forms
from localflavor.br.forms import BRZipCodeField


class AddressForm(forms.Form):
    cep = forms.CharField(label='CEP', max_length=9)
    rua = forms.CharField(label='Rua', max_length=100)
    bairro = forms.CharField(label='Bairro', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    estado = forms.CharField(label='Estado', max_length=100)
    ibge = forms.CharField(label='Ibge', max_length=100)

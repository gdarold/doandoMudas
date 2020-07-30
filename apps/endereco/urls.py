from django.conf.urls import url
from .views import EnderecoCreate, EnderecoList

urlpatterns = [
    url('endereco/new/', EnderecoCreate.as_view(), name='endereco'),
    url('endereco/list/', EnderecoList.as_view(), name='endereco_list'),

]
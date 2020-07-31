from django.conf.urls import url
from .views import EnderecoCreate, EnderecoList

urlpatterns = [
    url('new/', EnderecoCreate.as_view(), name='endereco'),
    url('list/', EnderecoList.as_view(), name='list_endereco'),

]
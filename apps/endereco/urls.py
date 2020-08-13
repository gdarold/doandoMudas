from django.conf.urls import url
from .views import EnderecoCreate, EnderecoList, EnderecoEdit, EnderecoDelete

urlpatterns = [
    url('new/', EnderecoCreate.as_view(), name='new_enderecos'),
    url('list/', EnderecoList.as_view(), name='list_enderecos'),
    url('update/<int:endereco>/', EnderecoEdit.as_view(), name='update_enderecos'),
    url('delete/<int:endereco>/', EnderecoDelete.as_view(), name='delete_enderecos'),

]
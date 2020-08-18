
from django.conf.urls import url
from .views import PessoaEdit, PessoaCreate, PessoaList, PessoaDelete

urlpatterns = [
    url('new/', PessoaCreate.as_view(), name='pessoa'),
    url('list/', PessoaList.as_view(), name='list_pessoa'),
    url('editar/<pk>', PessoaEdit.as_view(), name='edit'),
    url('delete_pessoa/<int:pk>/', PessoaDelete.as_view(), name='delete_pessoa'),

]
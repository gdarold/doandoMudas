
from django.conf.urls import url
from .views import PessoaEdit, PessoaCreate, PessoaList, PessoaDelete, Perfil

urlpatterns = [
    url('new/', PessoaCreate.as_view(), name='pessoa'),
    url('list/', PessoaList.as_view(), name='list_pessoa'),
    url('user/list/', Perfil.as_view(), name="profile"),
    url('editar/<pk>', PessoaEdit.as_view(), name='edit'),
    url('delete_pessoa/<int:pk>/', PessoaDelete.as_view(), name='delete_pessoa'),

]
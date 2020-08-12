
from django.conf.urls import url
from .views import PessoaEdit, PessoaCreate, PessoaList, PessoaDelete

urlpatterns = [
    url('new/', PessoaCreate.as_view(), name='pessoa'),
    url('list/', PessoaList.as_view(), name='list_pessoas'),
    url('update/<int:id>/', PessoaEdit.as_view(), name='edit_pessoas'),
    url('delete/<int:pk>/', PessoaDelete.as_view(), name='delete_pessoas'),

]
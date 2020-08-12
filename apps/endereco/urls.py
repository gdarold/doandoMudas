from django.conf.urls import url
from .views import EnderecoCreate, EnderecoList, EnderecoEdit

urlpatterns = [
    url('new/', EnderecoCreate.as_view(), name='endereco'),
    url('list/', EnderecoList.as_view(), name='list_endereco'),
    url('edit/<int:pk>/', EnderecoEdit.as_view(), name='edit_endereco'),

]
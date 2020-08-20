from django.conf.urls import url
from .views import DoacaoCreate, DoacaoDelete, DoacaoEdit, DoacaoList

urlpatterns = [
    url('new/', DoacaoCreate.as_view(), name='new_doacoes'),
    url('list/', DoacaoList.as_view(), name='list_doacoes'),
    url('update/<int:pk>/', DoacaoEdit.as_view(), name='update'),


]
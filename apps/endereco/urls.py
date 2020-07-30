from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url('endereco/', views.AddressFormView.as_view(), name='endereco')
]
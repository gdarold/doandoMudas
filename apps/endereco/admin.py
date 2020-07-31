from django.contrib import admin

# Register your models here.

from apps.endereco.models import Endereco

admin.site.register(Endereco)
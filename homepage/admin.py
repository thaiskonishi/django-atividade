from django.contrib import admin
from homepage.models import Fotografia
#aqui fazemos todas as configurações do admin que precisamos

class ListandoFotos(admin.ModelAdmin):
    list_display = ("id", "nome", "preco")
    search_fields = ("nome",)  #adicionando um campo de busca
# Register your models here.
admin.site.register(Fotografia, ListandoFotos)
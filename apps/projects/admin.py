from django.contrib import admin
from .models import NovoProjeto

# Register your models here.

class NovoProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome_projeto', 'media_anual', 'owner']

admin.site.register(NovoProjeto, NovoProjetoAdmin)

from django import forms
from .models import NovoProjeto

class NovoProjetoForm(forms.ModelForm):

    class Meta:
        model = NovoProjeto
        exclude = ('owner',)

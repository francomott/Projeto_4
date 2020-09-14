from django.db import models
from django.contrib.auth.models import User

#blank=True --> Não obrigatório 
#null=True --> Aceita um valor nulo 

# Create your models here.
class NovoProjeto(models.Model):
    nome_projeto = models.CharField('Nome do projeto', max_length=50)
    local = models.CharField('CEP', max_length=50)
    media_anual = models.CharField('Média anual de consumo', max_length=5)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('M', 'Monofásica'),
        ('B', 'Bifásica'),
        ('T', 'Trifásica'),
    )
    type = models.CharField('Tipo de Ligação', max_length=1, choices=TYPE_CHOICES)
   

    class Meta:
        verbose_name = 'Novo Projeto'
        ordering = ['id']   #ordenar pelo ID 
    
    def __str__(self):      #O que retorna  no admin, retornar o nome do projeyo
        return self.nome_projeto

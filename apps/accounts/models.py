from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    cell_phone = models.CharField('Celular', max_length=16)

    class Meta:
        verbose_name = 'Perfil do Usuário'

    def __str__(self):
        return self.user.username
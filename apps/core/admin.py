from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.

#admin.site.unregister(User)    #tira essas opções do admin do django
#admin.site.unregister(Group)


admin.site.site_header = 'Projeto3 TCC Login'
admin.site.site_title = 'Administração Projeto3'
admin.site.site_title = 'Administração Projeto3 - Aplicações'

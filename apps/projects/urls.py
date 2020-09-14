from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('adicionar/', views.add_project, name='add_project'),
    path('', views.list_projects, name='list_projects'),
    path('excluir/<int:id_project>', views.delete_project, name='delete_project'),
]

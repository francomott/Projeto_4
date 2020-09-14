from django.shortcuts import render, redirect
from .forms import NovoProjetoForm
from .models import NovoProjeto
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login')
def add_project(request):
    template_name = 'project/add_project.html'
    context = {}
    if request.method == 'POST':
        form = NovoProjetoForm(request.POST)        # Requisição POST = Submetendo dados para salvar no banco de dados (aula 54)
        if form.is_valid():                         # Requisição GET = exibir algo (ex: digitar uma url)
            f = form.save(commit=False)
            f.owner = request.user
    form = NovoProjetoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login')
def list_projects(request):
    template_name = 'project/list_projects.html'
    projects = NovoProjeto.objects.filter(owner=request.user)
    context = {
        'projects': projects
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login')
def delete_project(request, id_project):
    project = NovoProjeto.objects.get(id=id_project)
    if project.owner == request.user:
        project.delete()
    return redirect('project:list_projects')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



from .forms import UserForm, UserProfileForm
from .models import UserProfile


# Create your views here.


def add_user(request):
    template_name = 'accounts/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, "Usuário salvo com sucesso!")
    form = UserForm()
    context ['form'] = form 
    return render(request, template_name, context)


def user_login(request):
    template_name: 'accounts/user_login.html'
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'accounts/user_login.html', {})

@login_required(login_url='/contas/login')
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

@login_required(login_url='/contas/login')
def add_user_profile(request):
    template_name = 'accounts/add_user_profile.html'
    context = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, "Perfil alterado com sucesso!")
    form = UserProfileForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login')
def user_change_passoword(request):
    template_name = 'accounts/user_change_passoword.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Senha alterada com sucesso.")
            update_session_auth_hash(request, form.user)
        else:
            messages.error(request, "Não foi possível alterar a senha.")
    form = PasswordChangeForm(user=request.user)
    context['form'] = form 
    return render(request, template_name, context)

@login_required(login_url='/contas/login')
def list_user_profile(request):
    template_name = 'accounts/list_user_profile.html'
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login')
def change_user_profile(request, username):
    template_name = 'accounts/change_user_profile.html'
    context = {}
    profile = UserProfile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso.")
    form - UserProfileForm(instance=profile)
    context['form'] = form
    return render(request, template_name, context)
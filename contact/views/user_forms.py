from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Usuário registrado com sucesso!')
            form.save()
            return redirect('contact:login')

    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f'Bem-vindo {user.username}!')
            return redirect('contact:contact_home')
        messages.error(request, 'Credênciais inválidas!')

    context = {
        'form': form
    }

    return render(request, 'contact/login.html', context)


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Desconectado com sucesso!')
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados de usuário alterados com sucesso!')
            return redirect('contact:contact_home')
        messages.error(request, 'Não foi possível atualizar o usuário!')

    context = {
        'form': form
    }

    return render(request, 'contact/user_update.html', context)


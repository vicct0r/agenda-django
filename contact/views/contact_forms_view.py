from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from contact.models import Contato
from contact.forms import ContatoForm


@login_required(login_url='contact:login')
def create_contact(request):
    form_action = reverse('contact:contact_create') # URL do formulario de criação de Contato
    # este if é para caso o usuario tenha enviado os dados
    # ou seja, data=request.POST, data é o primeiro parâmetro que ContatoForm() recebe
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES) # request.POST passa os valores que estão no corpo da request para o formulário
        
        if form.is_valid():
            contact = form.save(commit=False) # passei form_save para variavel 'contact' para redirecionar para o contato que acabou de ser criado, com os valores do request.POST (corpo da requisição)
            contact.owner = request.user
            contact.save()
            messages.success(request, f'Contato "{form.cleaned_data.get('first_name')}" criado com sucesso!')
            return redirect('contact:contact_update', contact_id=contact.id) # passando o id de contact para gerar uma URL dinamica

        context = {
            'form': form, # Os dados do formulário preenchido virão aqui
            'form_action': form_action,
        }

        return render(request, 'contact/create.html', context)
    
    context = {
            'form': ContatoForm(), # Se não for POST, estamos renderizando o formulario vazio
            'form_action': form_action, 
        }

    return render(request, 'contact/create.html', context)


@login_required(login_url='contact:login')
def update_contact(request, contact_id):
    form_action = reverse('contact:contact_update', args=[contact_id]) # gerando uma URL dinamica para update do contato especifico
    contact = get_object_or_404(Contato, id=contact_id, owner=request.user) # encontrando o usuario que queremos editar pelo id que recebemos no corpo da URL (contato/3/update)

    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES, instance=contact) # instance indica que estamos editando um objeto existente
        if form.is_valid():
            form.save()
            messages.success(request, f'Contato "{form.cleaned_data.get('first_name')}" alterado com sucesso!')
            return redirect('contact:contact_update', contact_id=contact.id)
    else:
        form = ContatoForm(instance=contact)

    context = {
        'form': form,
        'form_action': form_action, 
    }
    return render(request, 'contact/create.html', context)


@login_required(login_url='contact:login')
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contato, id=contact_id, owner=request.user)
    

    if request.method == 'POST':
        messages.success(request, f'Contato "{contact.first_name}" foi removido com sucesso!')
        contact.delete()
        return redirect('contact:base_home')
    
    return HttpResponseNotAllowed(['POST'])
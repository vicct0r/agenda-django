from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from contact.models import Contato
from contact.forms import ContatoForm


def create(request):
    form_action = reverse('contact:contact_create') # URL do formulario de criação de Contato
    # este if é para caso o usuario tenha enviado os dados
    # ou seja, data=request.POST, data é o primeiro parâmetro que ContatoForm() recebe
    if request.method == 'POST':
        form = ContatoForm(request.POST) # request.POST passa os valores que estão no corpo da request para o formulário
        
        if form.is_valid():
            contact = form.save() # passei form_save para variavel 'contact' para redirecionar para o contato que acabou de ser criado, com os valores do request.POST (corpo da requisição)
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


def update(request, contact_id):
    form_action = reverse('contact:contact_update', args=[contact_id]) # gerando uma URL dinamica para update do contato especifico
    contact = get_object_or_404(Contato, id=contact_id) # encontrando o usuario que queremos editar pelo id que recebemos no corpo da URL (contato/3/update)

    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contact) # instance indica que estamos editando um objeto existente
        if form.is_valid():
            form.save()
            return redirect('contact:contact_update', contact_id=contact.id)
    else:
        form = ContatoForm(instance=contact)

    context = {
        'form': form,
        'form_action': form_action, 
    }
    return render(request, 'contact/create.html', context)

    

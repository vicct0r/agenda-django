from django.shortcuts import render
from contact.models import Contato

def index(request):
    contatos = Contato.objects.order_by('-id')

    context = {
        'contatos': contatos,
    }



    return render(request, 'contact/index.html', context)
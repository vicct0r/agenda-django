from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contato
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404


def home(request):
    contatos = Contato.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contatos, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'global/base.html', context)


def detail(request, contact_id):
    contato = get_object_or_404(Contato, pk=contact_id) 
    
    context = {
        'contato': contato
    }

    return render(request, 'contact/contact_detail.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return(redirect('contact:base_home'))

    contato = Contato.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contato, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'global/base.html', context)
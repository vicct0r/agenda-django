from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):

    form = RegisterForm()
    
    messages.info(request, 'Você acabou de entrar na página de registro!')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:contact_home')

    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context)
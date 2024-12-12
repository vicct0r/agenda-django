from django.shortcuts import render

def home(request):
    return render(request, 'global/base.html')


def index(request):
    return render(request, 'contact/index.html')
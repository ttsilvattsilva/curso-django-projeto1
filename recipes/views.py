from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html', status=404, context={
        'name': 'Thiago T Silva',
    })

def sobre(request):
    return render(request, 'recipes/contato.html')

def contato(request):
    return HttpResponse('CONTATO')
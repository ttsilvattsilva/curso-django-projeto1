from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return HttpResponse('CONTATO')
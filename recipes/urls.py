from django.urls import path
from django.http import HttpResponse
from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_home(request):
    return HttpResponse('<h1> Bem vindo a pj_produtos</h1>')

def view_produtos(request):
    return HttpResponse('<h1>Area de produtos</h1>') 

def view_clientes(request):
    return HttpResponse('<h1>Area de clientes</h1>')   
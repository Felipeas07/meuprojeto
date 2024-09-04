from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def cadastro(request):
    return render(request, 'myapp/cadastro.html')

def index(request):
    return render(request, 'myapp/index.html')

def cadastro(request):
    return render(request, 'myapp/cadastro.html')

def contato(request):
    return render(request, 'myapp/contato.html')

def depoimentos(request):
    return render(request, 'myapp/depoimentos.html')

def login_view(request):
    return render(request, 'myapp/login.html')

def logout_view(request):
    return render(request, 'myapp/logout.html')

def projetos(request):
    return render(request, 'myapp/projetos.html')

def servicos(request):
    return render(request, 'myapp/servicos.html')

def sobre(request):
    return render(request, 'myapp/sobre.html')
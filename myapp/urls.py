from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('index', permanent=False)),  # Redireciona a raiz para 'home'
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),  # Adicionado '/' no final
    path('contato/', views.contato, name='contato'),
    path('depoimentos/', views.depoimentos, name='depoimentos'),
    path('logout/', views.logout_view, name='logout'),
    path('projetos/', views.projetos, name='projetos'),
    path('servicos/', views.servicos, name='servicos'),
    path('sobre/', views.sobre, name='sobre'),
]

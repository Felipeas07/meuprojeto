from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('index', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contato/', views.contato, name='contato'),
    path('depoimentos/', views.depoimentos, name='depoimentos'),
    path('logout/', views.logout_view, name='logout'),
    path('projetos/', views.projetos, name='projetos'),
    path('servicos/', views.servicos, name='servicos'),
    path('sobre/', views.sobre, name='sobre'),
]
from django.contrib import admin
from django.urls import path

from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('painel/', views.dashboard, name='dashboard'),
    path('envia_email/', views.envia_email, name='envia_email'),
    path('usuarios/login/action', views.login_action, name='login_action'),
    path('usuarios/logout/action', views.logout_action, name='logout_action'),
    path('usuarios/login', views.login_form, name='login_form'),
    path('empresa/editar/<int:id>',
         views.editar_cadastro_empresa, name='editar_empresa'),
    path('empresa/listar', views.listar_cadastro_empresa, name='listar_empresa'),
    path('empresa/deletar/<int:id>',
         views.deletar_cadastro_empresa, name='deletar_empresa'),
]

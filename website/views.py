from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, render

from website.forms import EmailForm, EmpresaForm, LoginForm
from website.models import Empresa


def home(request):
    lista_empresa = Empresa.objects.all()
    for e in lista_empresa:
        e

    form = EmailForm()
    contexto = {'lista_empresa': e, 'form': form}
    return render(request, 'website/homepage/home.html', context=contexto)


def envia_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                'wendel.mariano@alfatransportes.com.br',
                [to_email],
                fail_silently=False,
            )

            messages.success(request, 'Mensagem Enviada!')
            return redirect('home')

    return redirect('home')


def dashboard(request):
    lista_empresa = Empresa.objects.all()
    for e in lista_empresa:
        e
    contexto = {'lista_empresa': e}
    return render(request, 'website/dashboard/dashboard.html', context=contexto)


def login_form(request):
    usuario_autenticado = request.user.is_authenticated
    if usuario_autenticado:
        return redirect('dashboard')

    formulario = LoginForm()
    context = {'formulario': formulario}
    return render(request, 'website/auth/login.html', context=context)


def login_action(request):
    if not request.POST:
        raise Http404()

    formulario = LoginForm(request.POST)

    if formulario.is_valid():
        username = formulario.cleaned_data.get('username')
        password = formulario.cleaned_data.get('password')
        usuario_autenticado = authenticate(
            username=username, password=password)

        if usuario_autenticado:
            login(request, usuario_autenticado)
            messages.success(request, 'Usuário logado com sucesso')
            return redirect('dashboard')

    messages.error(request, 'Usuário ou Senha inválido(a)')
    return redirect('login_form')


def logout_action(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login_form')
def criar_cadastro_empresa(request):
    empresa = Empresa()
    formulario = EmpresaForm(request.POST or None, files=request.FILES or None)

    if formulario.is_valid():
        empresa = formulario.save(commit=False)
        empresa.save()
        messages.success(request, 'Cadastro salvo com sucesso')
        return redirect('listar_empresa')

    contexto = {'formulario': formulario, 'action': 'create', 'id': 0}
    return render(request, 'website/dashboard/formulario-empresa.html', context=contexto)


@login_required(login_url='login_form')
def editar_cadastro_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    formulario = EmpresaForm(request.POST or None,
                             instance=empresa, files=request.FILES or None)

    if formulario.is_valid():
        empresa = formulario.save(commit=False)
        empresa.save()

        messages.success(request, 'Cadastro salvo com sucesso')
        return redirect('listar_empresa')

    contexto = {'formulario': formulario, 'action': 'update', 'id': id}
    return render(request, 'website/dashboard/formulario-empresa.html', context=contexto)


@login_required(login_url='login_form')
def listar_cadastro_empresa(request):
    lista_empresa = Empresa.objects.all()
    print(lista_empresa)
    contexto = {'lista_razao_social': lista_empresa}
    return render(request, 'website/dashboard/lista_empresa.html', context=contexto)


@login_required(login_url='login_form')
def deletar_cadastro_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.success(request, 'Empresa deletado com sucesso')
    return redirect('listar_empresa')

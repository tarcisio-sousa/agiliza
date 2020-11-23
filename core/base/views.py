from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PropostaForm
from .models import Proposta


def signin(request):
    is_auth = False
    msg = {}

    if request.user.id:
        return redirect(reverse('home'))
    elif request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if (user is not None) and (user.is_active):
            if user.is_superuser:
                login(request, user)
                is_auth = True

            if is_auth:
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect(reverse('home'))
        else:
            msg['erro'] = 'Usuário ou senha inválidos!'

    return render(request, 'base/sign_in.html')


def signout(request):
    logout(request)
    return redirect(reverse('signin'))


@login_required
def home(request):
    return render(request, 'base/home.html')


@login_required
def propostas(request):
    propostas = Proposta.objects.all()
    return render(request, 'base/propostas.html', {'propostas': propostas})


@login_required
def proposta(request, id=False):
    msg = {}

    proposta_form = PropostaForm()

    if (id):
        proposta = Proposta.objects.get(id=id)
        proposta_form = PropostaForm(instance=proposta)

    if request.method == 'POST':
        proposta_form = PropostaForm(request.POST)

        if id:
            proposta_form = PropostaForm(request.POST, instance=proposta)

        if proposta_form.is_valid():
            proposta = proposta_form.save()
            msg = {'sucesso': 'Proposta salva com sucesso!'}
            redirect(reverse('home'))
        else:
            msg = {'erro': 'Ocorreu alugm erro!'}

    return render(request, 'base/proposta.html', {'proposta_form': proposta_form, 'msg': msg})


@login_required
def proposta_documento(request, id):
    proposta = Proposta.objects.get(id=id)
    return render(request, 'base/proposta_documento.html', {'proposta': proposta})


@login_required
def declaracoes(request):
    return render(request, 'base/declaracoes.html')


@login_required
def convenios(request):
    return render(request, 'base/convenios.html')

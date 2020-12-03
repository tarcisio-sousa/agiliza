from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PropostaForm
from .models import Proposta, Convenio, Projeto


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
def proposta(request, id=False, situacao=False):

    if (situacao):
        proposta = Proposta.objects.get(id=id)
        proposta.situacao = situacao
        proposta.save()
        situacao = proposta.get_situacao_display()
        messages.add_message(request, messages.INFO, f'Proposta {proposta.numero} {situacao}')
        if proposta.situacao == 'empenhado':
            __gerar_convenio(request, proposta)
        return redirect(reverse('propostas'))

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
            messages.add_message(request, messages.SUCCESS, 'Proposta salva com sucesso!')
            return redirect(reverse('propostas'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Proposta salva com sucesso!')

    return render(request, 'base/proposta.html', {'proposta_form': proposta_form})


@login_required
def proposta_documento(request, id):
    proposta = Proposta.objects.get(id=id)
    return render(request, 'base/proposta_documento.html', {'proposta': proposta})


def __gerar_convenio(request, proposta):
    (convenio, gerado) = Convenio.objects.get_or_create(proposta=proposta)
    if gerado:
        messages.add_message(request, messages.SUCCESS, 'Convênio gerado com sucesso!')
    else:
        messages.add_message(request, messages.INFO, 'Esta proposta possui convênio!')


@login_required
def declaracoes(request):
    return render(request, 'base/declaracoes.html')


@login_required
def convenios(request):
    convenios = Convenio.objects.all()
    return render(request, 'base/convenios.html', {'convenios': convenios})


@login_required
def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'base/projetos.html', {'projetos': projetos})


@login_required
def projeto(request, id):
    projeto = Projeto.objects.get(id=id)
    # for item in projeto.item_set.all():
    #     for subitem in item.item_set.all():
    #         # for subitem in subitem.resposta_item_set.all():
    #         print(subitem.respostaitem_set.all())

    return render(request, 'base/projeto.html', {'projeto': projeto})

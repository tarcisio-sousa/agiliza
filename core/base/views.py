from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PropostaForm, ConvenioArquivoExtratoForm
from .forms import ProjetoForm, ItemForm, OpcaoForm, AlternativaForm, ItemAlternativaForm
from .models import Proposta, Convenio, Projeto, Item, Opcao, Alternativa, ItemAlternativa, Orgao, Prefeitura


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
            if user.is_superuser or user.profissional.cargo.descricao == 'PREFEITO':
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
def propostas(request, filter_situacao=False):
    choices_situacao = Proposta.SituacaoChoice.choices

    if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
        prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
        propostas = Proposta.objects.filter(prefeitura=prefeitura)
    else:
        propostas = Proposta.objects.all()

    if filter_situacao:
        propostas = propostas.filter(situacao=filter_situacao)

    if request.method == 'POST':
        if request.POST['search']:
            propostas = propostas.filter(Q(numero=request.POST['search']) | Q(objeto__contains=request.POST['search']))

    propostas = propostas.order_by('-id')

    return render(request, 'base/propostas.html', {
        'choices_situacao': choices_situacao, 'filter_situacao': filter_situacao, 'propostas': propostas
    })


@login_required
def proposta(request, id=False, situacao=False):

    if (situacao):
        proposta = Proposta.objects.get(id=id)
        proposta.situacao = situacao
        proposta.save()
        situacao = proposta.get_situacao_display()
        messages.add_message(request, messages.INFO, f'Proposta {proposta.numero} {situacao}')
        if proposta.situacao == 'empenhada':
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
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar a proposta!')

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
    if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
        prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
        convenios = Convenio.objects.filter(proposta__prefeitura=prefeitura)
    else:
        convenios = Convenio.objects.all()

    if request.method == 'POST':
        if request.POST['search']:
            convenios = convenios.filter(Q(numero_convenio=request.POST['search']) | Q(orgao=request.POST['search']))

    orgaos = Orgao.objects.all()
    return render(request, 'base/convenios.html', {'convenios': convenios, 'orgaos': orgaos})


@login_required
def arquivo_extrato(request, id):
    if request.method == 'POST':
        convenio = Convenio.objects.get(id=id)
        form = ConvenioArquivoExtratoForm(request.POST, request.FILES, instance=convenio)
        if form.is_valid():
            form.save()
    return redirect(reverse('convenios'))


@login_required
def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'base/projetos.html', {'projetos': projetos})


@login_required
def projeto(request, id=False):
    projeto_form = ProjetoForm()

    if (id):
        projeto = Projeto.objects.get(id=id)
        projeto_form = ProjetoForm(instance=projeto)

    if request.method == 'POST':

        projeto_form = ProjetoForm(request.POST)

        if id:
            projeto = Projeto.objects.get(id=id)
            projeto_form = ProjetoForm(request.POST, instance=projeto)

        if projeto_form.is_valid():
            projeto = projeto_form.save()
            messages.add_message(request, messages.SUCCESS, 'Projeto salvo com sucesso!')
            return redirect(reverse('projetos'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o projeto!')

    return render(request, 'base/projeto.html', {'projeto_form': projeto_form})


@login_required
def projeto_itens(request, id=False):
    itens = Item.objects.filter(projeto=id)
    return render(request, 'base/itens.html', {'itens': itens})


@login_required
def itens(request, id=False):
    itens = Item.objects.all()
    return render(request, 'base/itens.html', {'itens': itens})


@login_required
def item(request, id=False):
    item_form = ItemForm()

    if (id):
        item = Item.objects.get(id=id)
        item_form = ItemForm(instance=item)

    if request.method == 'POST':

        item_form = ItemForm(request.POST)

        if id:
            item = Item.objects.get(id=id)
            item_form = ItemForm(request.POST, instance=item)

        if item_form.is_valid():
            item = item_form.save()
            messages.add_message(request, messages.SUCCESS, 'Item salvo com sucesso!')
            return redirect(reverse('itens'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o item!')

    return render(request, 'base/item.html', {'item_form': item_form})


@login_required
def opcoes(request):
    opcoes = Opcao.objects.all()
    return render(request, 'base/opcoes.html', {'opcoes': opcoes})


@login_required
def opcao(request, id=False):
    opcao_form = OpcaoForm()

    if (id):
        opcao = Opcao.objects.get(id=id)
        opcao_form = OpcaoForm(instance=opcao)

    if request.method == 'POST':

        opcao_form = OpcaoForm(request.POST)

        if id:
            opcao = Opcao.objects.get(id=id)
            opcao_form = OpcaoForm(request.POST, instance=opcao)

        if opcao_form.is_valid():
            opcao = opcao_form.save()
            messages.add_message(request, messages.SUCCESS, 'Opção salva com sucesso!')
            return redirect(reverse('opcoes'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar a opção!')

    return render(request, 'base/opcao.html', {'opcao_form': opcao_form})


@login_required
def alternativas(request):
    alternativas = Alternativa.objects.all()
    return render(request, 'base/alternativas.html', {'alternativas': alternativas})


@login_required
def alternativa(request, id=False):
    alternativa_form = AlternativaForm()

    if (id):
        alternativa = Alternativa.objects.get(id=id)
        alternativa_form = AlternativaForm(instance=alternativa)

    if request.method == 'POST':

        alternativa_form = AlternativaForm(request.POST)

        if id:
            alternativa = Alternativa.objects.get(id=id)
            alternativa_form = AlternativaForm(request.POST, instance=alternativa)

        if alternativa_form.is_valid():
            alternativa = alternativa_form.save()
            messages.add_message(request, messages.SUCCESS, 'Alternativa salva com sucesso!')
            return redirect(reverse('alternativas'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar a alternativa!')

    return render(request, 'base/alternativa.html', {'alternativa_form': alternativa_form})


@login_required
def itens_alternativas(request):
    itens = ItemAlternativa.objects.all()
    return render(request, 'base/itens_alternativas.html', {'itens': itens})


@login_required
def item_alternativas(request, id=False):
    item_alternativa_form = ItemAlternativaForm()

    if (id):
        item_alternativa = ItemAlternativa.objects.get(id=id)
        item_alternativa_form = ItemAlternativaForm(instance=item_alternativa)

    if request.method == 'POST':

        item_alternativa_form = ItemAlternativaForm(request.POST)

        if id:
            item_alternativa = ItemAlternativa.objects.get(id=id)
            item_alternativa_form = ItemAlternativaForm(request.POST, instance=item_alternativa)

        if item_alternativa_form.is_valid():
            item_alternativa = item_alternativa_form.save()
            messages.add_message(request, messages.SUCCESS, 'Item alternativa salva com sucesso!')
            return redirect(reverse('itensalternativas'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o item alternativa!')

    return render(request, 'base/item_alternativas.html', {'item_alternativa_form': item_alternativa_form})


@login_required
def check_list(request, id=False):
    projeto = Projeto.objects.get(pk=id)
    itens = Item.objects.filter(projeto__id=id)
    usuarios = User.objects.all()
    return render(request, 'base/check_list.html', {'projeto': projeto, 'itens': itens, 'usuarios': usuarios})


'''
@login_required
def projetos(request):
    projetos = Pavimentacao.objects.all()
    return render(request, 'base/projetos.html', {'projetos': projetos})


@login_required
def projeto(request, id=False):
    if id:
        if (request.POST['tipo_projeto'] == 'edificacao'):
            projeto = Edificacao()
        elif (request.POST['tipo_projeto'] == 'estradas'):
            projeto = Estrada()
        elif (request.POST['tipo_projeto'] == 'equipamento'):
            projeto = Equipamento()
        elif (request.POST['tipo_projeto'] == 'pavimentacao'):
            projeto = Pavimentacao()

        convenio = Convenio.objects.get(id=id)
        orgao = Orgao.objects.get(id=request.POST['orgao'])
        projeto.orgao = orgao
        projeto.convenio = convenio
        projeto.tipo = request.POST['tipo_projeto']
        projeto.save()
        return redirect(reverse('convenios'))

    return render(request, 'base/projeto.html')


@login_required
def projeto_estrada(request, id=False):

    projeto_form = EstradaForm()

    if id:
        projeto = Estrada.objects.get(id=id)
        projeto_form = EstradaForm(instance=projeto)

    if request.method == 'POST':
        projeto_form = EstradaForm(request.POST)

        if id:
            projeto_form = EstradaForm(request.POST, instance=projeto)

        if projeto_form.is_valid():
            projeto_form.save()
            messages.add_message(request, messages.SUCCESS, 'Checklist de projeto salvo com sucesso!')
            return redirect(reverse('projetos'))
        else:
            messages.add_message(
                request, messages.ERROR, 'Não foi possível salvar o checklist, verifique todos os itens!'
            )

    return render(request, 'base/projeto_estrada.html', {'projeto_form': projeto_form})


@login_required
def projeto_edificacao(request, id=False):

    projeto_form = EdificacaoForm()

    if id:
        projeto = Edificacao.objects.get(id=id)
        projeto_form = EdificacaoForm(instance=projeto)

    if request.method == 'POST':
        projeto_form = EdificacaoForm(request.POST)

        if id:
            projeto_form = EdificacaoForm(request.POST, instance=projeto)

        if projeto_form.is_valid():
            projeto_form.save()
            messages.add_message(request, messages.SUCCESS, 'Checklist de projeto salvo com sucesso!')
            return redirect(reverse('projetos'))
        else:
            messages.add_message(
                request, messages.ERROR, 'Não foi possível salvar o checklist, verifique todos os itens!')

    return render(request, 'base/projeto_edificacao.html', {'projeto_form': projeto_form})


@login_required
def projeto_equipamento(request, id=False):

    projeto_form = EquipamentoForm()

    if id:
        projeto = Equipamento.objects.get(id=id)
        projeto_form = EquipamentoForm(instance=projeto)

    if request.method == 'POST':
        projeto_form = EquipamentoForm(request.POST)

        if id:
            projeto_form = EquipamentoForm(request.POST, instance=projeto)

        if projeto_form.is_valid():
            projeto_form.save()
            messages.add_message(request, messages.SUCCESS, 'Checklist de projeto salvo com sucesso!')
            return redirect(reverse('projetos'))
        else:
            messages.add_message(
                request, messages.ERROR, 'Não foi possível salvar o checklist, verifique todos os itens!')

    return render(request, 'base/projeto_equipamento.html', {'projeto_form': projeto_form})


@login_required
def projeto_pavimentacao(request, id=False):

    projeto_form = PavimentacaoForm()

    if id:
        projeto = Pavimentacao.objects.get(id=id)
        projeto_form = PavimentacaoForm(instance=projeto)

    if request.method == 'POST':
        projeto_form = PavimentacaoForm(request.POST)

        if id:
            projeto_form = PavimentacaoForm(request.POST, instance=projeto)

        if projeto_form.is_valid():
            projeto_form.save()
            messages.add_message(request, messages.SUCCESS, 'Checklist de projeto salvo com sucesso!')
            return redirect(reverse('projetos'))
        else:
            messages.add_message(
                request, messages.ERROR, 'Não foi possível salvar o checklist, verifique todos os itens!'
            )

    return render(request, 'base/projeto_pavimentacao.html', {'projeto_form': projeto_form})
'''

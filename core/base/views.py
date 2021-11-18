from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.formats import localize
from .forms import PropostaForm, PropostaArquivoExtratoForm, PropostaValorLiberado, ConvenioArquivoExtratoForm
from .forms import ProjetoForm, OpcaoForm, AlternativaForm, ItemAlternativaForm, AtividadeForm, LicenciamentoForm
from .forms import ProjetoControleForm, ProjetoControleItemForm, ItemForm
from .models import Proposta, Convenio, Projeto, Item, Opcao, Alternativa, ItemAlternativa, Orgao, Prefeitura
from .models import Atividade, LicenciamentoAmbiental, Responsavel, ProjetoControle, ProjetoControleItem
from .models import TecnicoOrgao


def notification_scheduled_job():
    send_mail(
        'Proposta Cadastrada',
        'Agiliza Convênios - Proposta cadastrada com sucesso',
        'sousa.tarcisio.s@gmail.com',
        ['tarcisio.sales@bol.com.br', 'lucasdantas.eng@gmail.com'],
        fail_silently=False)


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
            if user.is_superuser or user.profissional:
                login(request, user)
                is_auth = True

            if is_auth:
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect(reverse('home'))
        else:
            msg['erro'] = 'Usuário ou senha inválidos!'

    return render(
        request,
        'base/sign_in.html')


def signout(request):
    logout(request)
    return redirect(reverse('signin'))


@login_required
def home(request):
    return render(
        request,
        'base/home.html')


@login_required
def propostas(request, filter_situacao=False):
    choices_situacao = Proposta.SituacaoChoice.choices
    propostas = Proposta.objects.filter(status=True).order_by('-id')

    if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
        prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
        propostas = propostas.filter(prefeitura=prefeitura)

    propostas = propostas.filter(
        situacao=filter_situacao) if filter_situacao else propostas

    if request.method == 'GET':
        if 'search' in request.GET:
            propostas = propostas.filter(Q(numero=request.GET['search']) | Q(objeto__contains=request.GET['search']))

    orgaos = Orgao.objects.all()
    projetos = Projeto.objects.all()

    return render(
        request,
        'base/propostas.html',
        {
            'choices_situacao': choices_situacao,
            'filter_situacao': filter_situacao,
            'propostas': propostas,
            'orgaos': orgaos,
            'projetos': projetos,
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
            _gerar_convenio(request, proposta)
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
            proposta = proposta_form.save(commit=False)
            proposta.status = True
            proposta.save()
            messages.add_message(request, messages.SUCCESS, 'Proposta salva com sucesso!')

            # send_mail(
            #     'Proposta Cadastrada',
            #     'Agiliza Convênios > Proposta cadastrada com sucesso',
            #     'sousa.tarcisio.s@gmail.com',
            #     ['tarcisio.sales@bol.com.br', ],
            #     fail_silently=False)

            return redirect(reverse('propostas'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar a proposta!')

    return render(request, 'base/proposta.html', {'proposta_form': proposta_form})


@login_required
def proposta_arquivo_extrato(request, id):
    if request.method == 'POST':
        proposta = Proposta.objects.get(id=id)
        proposta_arquivo_extrato_form = PropostaArquivoExtratoForm(request.POST, request.FILES, instance=proposta)
        if proposta_arquivo_extrato_form.is_valid():
            proposta_arquivo_extrato_form.save()
    return redirect(reverse('propostas'))


@login_required
def proposta_empenhar(request, id):
    if request.method == 'POST':
        proposta = Proposta.objects.get(id=id)
        proposta.situacao = 'empenhada'
        proposta.save()
        situacao = proposta.get_situacao_display()
        messages.add_message(request, messages.INFO, f'Proposta {proposta.numero} {proposta.objeto} {situacao}')
        if proposta.situacao == 'empenhada':
            dados = request.POST
            _gerar_convenio(request, proposta, dados)
        return redirect(reverse('propostas'))


@login_required
def proposta_documento(request, id):
    proposta = Proposta.objects.get(id=id)
    return render(request, 'base/proposta_documento.html', {'proposta': proposta})


def _gerar_convenio(request, proposta, dados):
    (convenio, gerado) = Convenio.objects.get_or_create(proposta=proposta)
    if gerado:
        if (dados['numero']):
            convenio.numero = dados['numero']
            convenio.status = True
            if (dados['nome']):
                tecnico_orgao = TecnicoOrgao()
                tecnico_orgao.nome = dados['nome']
                tecnico_orgao.telefone = dados['telefone']
                tecnico_orgao.save()
                convenio.tecnico_orgao = tecnico_orgao
            convenio.save()
            messages.add_message(request, messages.SUCCESS, 'Convênio gerado com sucesso!')
            _gerar_projeto(request, convenio, dados)
    else:
        messages.add_message(request, messages.INFO, 'Esta proposta possui convênio!')


def _gerar_projeto(request, convenio, dados):
    (controle, gerado) = ProjetoControle.objects.get_or_create(convenio=convenio)
    if gerado:
        controle.orgao_id = dados['orgao_id']
        controle.projeto_id = dados['projeto_id']
        controle.save()
        messages.add_message(request, messages.SUCCESS, 'Controle de projeto criado com sucesso!')
    else:
        messages.add_message(request, messages.INFO, 'Este controle possui projeto')


@login_required
def declaracoes(request):
    return render(request, 'base/declaracoes.html')


@login_required
def convenios(request):
    convenios = Convenio.objects.filter(status=True).order_by('-proposta__data')
    if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
        prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
        convenios = convenios.filter(proposta__prefeitura=prefeitura)

    if request.method == 'POST':
        if request.POST['search']:
            convenios = convenios.filter(
                Q(numero=request.POST['search']) | Q(orgao=request.POST['search']))

    orgaos = Orgao.objects.all()
    return render(
        request,
        'base/convenios.html',
        {
            'convenios': convenios,
            'orgaos': orgaos,
        })


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
    return render(
        request,
        'base/projetos.html',
        {
            'projetos': projetos,
        })


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
    projeto = Projeto.objects.get(id=id)
    itens = Item.objects.filter(projeto=projeto.id)
    return render(request, 'base/projeto_itens.html', {'projeto': projeto, 'itens': itens})


@login_required
def projeto_item(request, projeto_id, id=False):
    projeto = Projeto.objects.get(id=projeto_id)
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
            return redirect(reverse('projeto_itens', args=[projeto.id]))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o item!')

    return render(request, 'base/item.html', {'projeto': projeto, 'item_form': item_form})


@login_required
def itens(request, id=False):
    itens = Item.objects.all()
    return render(
        request,
        'base/itens.html',
        {
            'itens': itens,
        })


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
    return render(
        request,
        'base/opcoes.html',
        {
            'opcoes': opcoes,
        })


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
    return render(
        request,
        'base/alternativas.html',
        {
            'alternativas': alternativas,
        })


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
    return render(
        request,
        'base/itens_alternativas.html',
        {
            'itens': itens,
        })


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
    responsaveis = Responsavel.objects.all()
    return render(request, 'base/check_list.html', {'projeto': projeto, 'itens': itens, 'responsaveis': responsaveis})


@login_required
def convenio_projeto_controle(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    projeto_controle_item_form = ProjetoControleItemForm()
    try:
        controle = ProjetoControle.objects.get(convenio__id=convenio.id)
    except Exception:
        controle = False

    itens = False

    if (controle):
        itens = Item.objects.filter(projeto=controle.projeto)
        for item in itens:
            try:
                item.item_controle = ProjetoControleItem.objects.get(controle=controle, item=item)
            except Exception:
                item.item_controle = False

    return render(
        request, 'base/convenio_projeto_controle.html', {
            'convenio': convenio,
            'controle': controle,
            'itens': itens,
            'projeto_controle_item_form': projeto_controle_item_form
        })


@login_required
def projeto_controle(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    projeto_controle_form = ProjetoControleForm(initial={'convenio': convenio})

    if request.method == 'POST':
        projeto_controle_form = ProjetoControleForm(request.POST)

        if projeto_controle_form.is_valid():
            controle = projeto_controle_form.save(commit=False)
            controle.convenio = convenio
            controle.save()
            messages.add_message(request, messages.SUCCESS, 'Controle criado com sucesso!')
            return redirect(reverse('convenio_projeto_controle', args=[convenio_id]))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o controle!')
    return render(request, 'base/projeto_controle.html', {
        'convenio': convenio,
        'projeto_controle_form': projeto_controle_form
    })


@login_required
def projeto_controle_item(request, controle_id=False):
    controle = ProjetoControle.objects.get(id=controle_id)
    projeto_controle_item_form = ProjetoControleItemForm()

    if request.method == 'POST':

        projeto_controle_item_form = ProjetoControleItemForm(request.POST)

        if projeto_controle_item_form.is_valid():
            projeto_controle_item = projeto_controle_item_form.save(commit=False)
            projeto_controle_item.controle = controle
            projeto_controle_item.save()
            messages.add_message(request, messages.SUCCESS, 'Item adicionado com sucesso!')
            return redirect(reverse('convenio_projeto_controle', args=[controle.convenio.id]))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o item de controle!')

    return render(
        request,
        'base/projeto_controle_item.html',
        {
            'controle': controle,
            'projeto_controle_item_form': projeto_controle_item_form,
        }
    )


@login_required
def protocolo(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    atividades = Atividade.objects.filter(convenio=convenio)
    licenciamentos = LicenciamentoAmbiental.objects.filter(convenio=convenio)

    proposta_form = PropostaValorLiberado(instance=convenio.proposta)
    if request.method == 'POST':
        proposta_form = PropostaValorLiberado(request.POST, instance=convenio.proposta)
        if proposta_form.is_valid():
            proposta = proposta_form.save()
            messages.add_message(request, messages.SUCCESS, 'Valor liberado R$ %s' % localize(proposta.valor_liberado))
            return redirect(reverse('protocolo', args=[convenio.id]))

    return render(
        request,
        'base/protocolo.html',
        {
            'convenio': convenio,
            'atividades': atividades,
            'licenciamentos': licenciamentos,
            'proposta_form': proposta_form,
        })


@login_required
def atividades(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    atividade_form = AtividadeForm()
    if request.method == 'POST':
        atividade_form = AtividadeForm(request.POST, request.FILES)
        if atividade_form.is_valid():
            atividade = atividade_form.save(commit=False)
            atividade.convenio = convenio
            atividade.save()
            return redirect(reverse('protocolo', args=[convenio.id]))

    return render(
        request,
        'base/atividade.html',
        {
            'convenio': convenio,
            'atividade_form': atividade_form,
        })


@login_required
def licenciamentos_ambientais(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    licenciamento_form = LicenciamentoForm()
    if request.method == 'POST':
        licenciamento_form = LicenciamentoForm(request.POST, request.FILES)
        if licenciamento_form.is_valid():
            licenciamento = licenciamento_form.save(commit=False)
            licenciamento.convenio = convenio
            licenciamento.save()
            return redirect(reverse('protocolo', args=[convenio.id]))

    return render(
        request,
        'base/licenciamento_ambiental.html',
        {
            'convenio': convenio,
            'licenciamento_form': licenciamento_form,
        })

from datetime import date, datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Count, Q, Sum
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.formats import localize

from .forms import (AlternativaForm, AtividadeForm,
                    ConvenioAprovacaoLicitacaoForm, ConvenioArquivoExtratoForm,
                    ConvenioRecursoContaForm, ItemAlternativaForm, ItemForm,
                    LicenciamentoForm, OpcaoForm, ProjetoControleForm,
                    ProjetoControleItemForm, ProjetoForm,
                    PropostaArquivoExtratoForm, PropostaForm,
                    PropostaValorLiberado, ProtocoloDadosBancariosForm,
                    ProtocoloEmpresaContratadaForm,
                    ProtocoloExecucaoConcedenteForm,
                    ProtocoloExecucaoConvenenteForm, ProtocoloForm,
                    ServicoForm)
from .models import (Alternativa, Atividade, Convenio, ExecucaoConcedente,
                     ExecucaoConvenente, Item, ItemAlternativa,
                     LicenciamentoAmbiental, Opcao, Orgao, Prefeitura, Projeto,
                     ProjetoControle, ProjetoControleItem, Proposta, Protocolo,
                     Responsavel, Servico, TecnicoOrgao)


def notification_scheduled_job():
    send_mail(
        'Proposta Cadastrada',
        'Agiliza Convênios - Proposta cadastrada com sucesso',
        'sousa.tarcisio.s@gmail.com',
        ['tarcisio.sales@bol.com.br', ],
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

        if (user is not None) and user.is_active:
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


def cria_lista_situacoes(situacoes):
    resultado = {}
    for [chave, situacao] in situacoes:
        resultado[chave] = {'situacao': situacao, 'situacao__count': 0, 'valor_convenio__sum': 0.0}
    return resultado


def cria_tabela_situacoes(situacoes, total):
    for situacao in total:
        situacoes[situacao['situacao']]['situacao__count'] = situacao['situacao__count']
        situacoes[situacao['situacao']]['valor_convenio__sum'] = situacao['valor_convenio__sum']
    return situacoes


@login_required
def home(request):
    lista_situacoes = Proposta.SituacaoChoice.choices
    resultado_situacoes = cria_lista_situacoes(lista_situacoes)
    busca_total_propostas_situacao = Proposta.objects.values('situacao').annotate(
        Count('situacao'), Sum('valor_convenio'))
    situacoes = cria_tabela_situacoes(resultado_situacoes, busca_total_propostas_situacao)

    data = {
        'total_prefeitura': Prefeitura.objects.count(),
        'total_proposta': Proposta.objects.count(),
        'total_convenio': Convenio.objects.count(),
        'total_servico': Servico.objects.count(),
        # 'lista_propostas_situacao': situacoes,
        'situacoes': situacoes
    }

    return render(
        request,
        'base/home.html', {'data': data})


@login_required
def propostas(request):
    filter_situacao = False
    filter_prefeitura = False
    choices_situacao = Proposta.SituacaoChoice.choices
    choices_prefeitura = Prefeitura.objects.all()
    propostas = Proposta.objects.filter(status=True).order_by('-data__year', '-id')

    if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
        prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
        propostas = propostas.filter(prefeitura=prefeitura)

    if request.method == 'GET':
        if 'search' in request.GET:
            propostas = propostas.filter(
                Q(numero=request.GET['search']) |
                Q(objeto__contains=request.GET['search']) |
                Q(prefeitura__nome__contains=request.GET['search']))
        if 'situacao' in request.GET:
            filter_situacao = request.GET['situacao']
            propostas = propostas.filter(situacao=filter_situacao)
        if 'prefeitura' in request.GET:
            filter_prefeitura = int(request.GET['prefeitura'])
            propostas = propostas.filter(prefeitura=filter_prefeitura)

    paginator = Paginator(propostas, 10)

    page_number = request.GET.get('page')
    propostas = paginator.get_page(page_number)

    orgaos = Orgao.objects.all()
    projetos = Projeto.objects.all()

    return render(
        request,
        'base/propostas.html',
        {
            'choices_situacao': choices_situacao,
            'filter_situacao': filter_situacao,
            'choices_prefeitura': choices_prefeitura,
            'filter_prefeitura': filter_prefeitura,
            'propostas': propostas,
            'orgaos': orgaos,
            'projetos': projetos,
        })


@login_required
def proposta(request, id=False, situacao=False):

    if situacao:
        proposta = Proposta.objects.get(id=id)
        proposta.situacao = situacao
        proposta.save()
        situacao = proposta.get_situacao_display()
        messages.add_message(request, messages.INFO, f'Proposta {proposta.numero} {situacao}')
        if proposta.situacao == 'empenhada':
            _gerar_convenio(request, proposta)
        return redirect(reverse('propostas'))

    proposta_form = PropostaForm()

    if id:
        proposta = Proposta.objects.get(id=id)
        proposta_form = PropostaForm(
            instance=proposta, initial={'auto_complete_prefeitura': proposta.prefeitura})

    if request.method == 'POST':
        proposta_form = PropostaForm(request.POST)

        if id:
            proposta_form = PropostaForm(
                request.POST, instance=proposta, initial={'auto_complete_prefeitura': proposta.prefeitura})

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
        if dados['numero']:
            convenio.numero = dados['numero']
            convenio.data_suspensiva = datetime.strptime(dados['data_suspensiva'], '%d/%m/%Y')
            convenio.data_vigencia = datetime.strptime(dados['data_vigencia'], '%d/%m/%Y')
            convenio.orgao_id = dados['orgao_id']
            convenio.banco = dados['banco']
            convenio.agencia = dados['agencia']
            convenio.conta = dados['conta']
            convenio.status = True
            if dados['nome']:
                if dados['tecnico_orgao_id']:
                    tecnico_orgao = TecnicoOrgao.objects.get(id=dados['tecnico_orgao_id'])
                else:
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
def proposta_excluir(request, id):
    proposta = Proposta.objects.get(id=id)
    proposta.delete()
    messages.add_message(request, messages.INFO, 'Proposta excluída com sucesso!')
    return redirect(reverse('propostas'))


@login_required
def declaracoes(request):
    return render(request, 'base/declaracoes.html')


@login_required
def convenios(request):
    search = request.GET['search'] if 'search' in request.GET else None
    [order_by, order] = request.GET['order_by'].split(',') if 'order_by' in request.GET else [None, None]
    filter_prefeitura = False
    choices_prefeitura = Prefeitura.objects.all()
    prefeitura = None
    convenios = Convenio.objects.filter(status=True).order_by('-proposta__data')

    if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
        prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
        convenios = convenios.filter(proposta__prefeitura=prefeitura)

    if request.method == 'GET':
        if 'prefeitura' in request.GET:
            filter_prefeitura = int(request.GET['prefeitura'])
            convenios = convenios.filter(proposta__prefeitura=filter_prefeitura)
        if search:
            convenios = convenios.filter(
                Q(numero__contains=search) |
                Q(orgao__descricao=search) |
                Q(proposta__objeto__contains=search))
        if order_by:
            order_description = order_by
            if order == 'desc':
                order_description = '-' + order_by
            convenios = convenios.order_by(order_description)

    for convenio in convenios:
        protocolo = Protocolo.objects.filter(convenio_id=convenio.id).order_by('-data').first()
        convenio.protocolo = protocolo
        if protocolo:
            data = protocolo.data
        else:
            data = convenio.data_criacao
        convenio.dias = abs((date.today() - data).days)

    paginator = Paginator(convenios, 10)

    page_number = request.GET.get('page')
    convenios = paginator.get_page(page_number)

    orgaos = Orgao.objects.all()
    return render(
        request,
        'base/convenios.html',
        {
            'choices_prefeitura': choices_prefeitura,
            'filter_prefeitura': filter_prefeitura,
            'user_prefeitura': prefeitura,
            'convenios': convenios,
            'orgaos': orgaos,
            'search': search,
            'order': order,
        })


@login_required
def convenio_excluir(request, id):
    convenio = Convenio.objects.get(id=id)
    convenio.delete()
    messages.add_message(request, messages.INFO, 'Convênio excluído com sucesso!')
    return redirect(reverse('convenios'))


@login_required
def convenio_aprovar_projeto(request, id):
    if request.method == 'POST':
        dados = request.POST
        convenio = Convenio.objects.get(id=id)
        convenio.data_aprovacao_projeto = datetime.strptime(dados['data_aprovacao_projeto'], '%d/%m/%Y')
        convenio.situacao = 'projeto-aprovado'
        convenio.save()
        protocolos = Protocolo(
            convenio=convenio,
            data=convenio.data_aprovacao_projeto,
            data_prevista=convenio.data_aprovacao_projeto,
            data_protocolado=convenio.data_aprovacao_projeto,
            consideracoes=convenio.get_situacao_display())
        protocolos.save()
        situacao = convenio.get_situacao_display()
        messages.add_message(
            request,
            messages.INFO,
            f'Convênio {convenio.numero} {convenio.proposta.objeto} ({situacao})')
        return redirect(reverse('convenios'))


@login_required
def convenio_licitar_projeto(request, id):
    if request.method == 'POST':
        dados = request.POST
        convenio = Convenio.objects.get(id=id)
        convenio.data_licitacao_projeto = datetime.strptime(dados['data_licitacao_projeto'], '%d/%m/%Y')
        convenio.situacao = 'aguardando-aceite-licitacao'
        convenio.save()
        protocolos = Protocolo(
            convenio=convenio,
            data=convenio.data_licitacao_projeto,
            data_prevista=convenio.data_licitacao_projeto,
            data_protocolado=convenio.data_licitacao_projeto,
            consideracoes=convenio.get_situacao_display())
        protocolos.save()
        situacao = convenio.get_situacao_display()
        messages.add_message(
            request,
            messages.INFO,
            f'Convênio {convenio.numero} {convenio.proposta.objeto} ({situacao})')
        return redirect(reverse('convenios'))


@login_required
def convenio_aprovar_licitacao(request, id):
    if request.method == 'POST':
        convenio = Convenio.objects.get(id=id)
        convenio_form = ConvenioAprovacaoLicitacaoForm(request.POST, instance=convenio)
        if convenio_form.is_valid():
            convenio = convenio_form.save(commit=False)
            convenio.situacao = 'licitacao-aprovada'
            convenio.save()
            protocolos = Protocolo(
                convenio=convenio,
                data=convenio.data_aceite_licitacao,
                data_prevista=convenio.data_aceite_licitacao,
                data_protocolado=convenio.data_aceite_licitacao,
                consideracoes=convenio.get_situacao_display())
            protocolos.save()
            situacao = convenio.get_situacao_display()
            messages.add_message(
                request,
                messages.INFO,
                f'Convênio {convenio.numero} {convenio.proposta.objeto} ({situacao})')
        return redirect(reverse('convenios'))


@login_required
def convenio_recurso_conta(request, id):
    if request.method == 'POST':
        convenio = Convenio.objects.get(id=id)

        # convenio.data_liberacao_recurso = datetime.strptime(dados['data_liberacao_recurso'], '%d/%m/%Y')
        # convenio.valor_recurso = localize(dados['valor_recurso'])
        # convenio.save()
        convenio_form = ConvenioRecursoContaForm(request.POST, instance=convenio)
        if convenio_form.is_valid():
            convenio = convenio_form.save(commit=False)
            convenio.situacao = 'recurso-em-conta'
            convenio.save()

            protocolos = Protocolo(
                convenio=convenio,
                data=convenio.data_liberacao_recurso,
                data_prevista=convenio.data_liberacao_recurso,
                data_protocolado=convenio.data_liberacao_recurso,
                consideracoes=convenio.get_situacao_display())
            protocolos.save()
            situacao = convenio.get_situacao_display()
            messages.add_message(
                request,
                messages.INFO,
                f'Convênio {convenio.numero} {convenio.proposta.objeto} ({situacao})')
        return redirect(reverse('convenios'))


@login_required
def convenio_concluir(request, id):
    if request.method == 'POST':
        dados = request.POST
        convenio = Convenio.objects.get(id=id)
        convenio.data_conclusao = datetime.strptime(dados['data_conclusao'], '%d/%m/%Y')
        convenio.situacao = 'convenio-concluido'
        convenio.save()
        protocolos = Protocolo(
            convenio=convenio,
            data=convenio.data_conclusao,
            data_prevista=convenio.data_conclusao,
            data_protocolado=convenio.data_conclusao,
            consideracoes=convenio.get_situacao_display())
        protocolos.save()
        situacao = convenio.get_situacao_display()
        messages.add_message(
            request,
            messages.INFO,
            f'Convênio {convenio.numero} {convenio.proposta.objeto} ({situacao})')
        return redirect(reverse('convenios'))


@login_required
def convenio_concluir_prestacao_contas(request, id):
    if request.method == 'POST':
        dados = request.POST
        convenio = Convenio.objects.get(id=id)
        convenio.data_prestacao_contas = datetime.strptime(dados['data_prestacao_contas'], '%d/%m/%Y')
        convenio.situacao = 'prestacao-de-contas-concluida'
        convenio.save()
        protocolos = Protocolo(
            convenio=convenio,
            data=convenio.data_prestacao_contas,
            data_prevista=convenio.data_prestacao_contas,
            data_protocolado=convenio.data_prestacao_contas,
            consideracoes=convenio.get_situacao_display())
        protocolos.save()
        situacao = convenio.get_situacao_display()
        messages.add_message(
            request,
            messages.INFO,
            f'Convênio {convenio.numero} {convenio.proposta.objeto} ({situacao})')
        return redirect(reverse('convenios'))


@login_required
def arquivo_extrato(request, id):
    if request.method == 'POST':
        convenio = Convenio.objects.get(id=id)
        form = ConvenioArquivoExtratoForm(request.POST, request.FILES, instance=convenio)
        if form.is_valid():
            form.save()
    return redirect(reverse('convenios'))


@login_required
def servicos(request):
    servicos = Servico.objects.filter(status=True).order_by('-data_cadastro')

    paginator = Paginator(servicos, 10)

    page_number = request.GET.get('page')
    servicos = paginator.get_page(page_number)

    return render(
        request,
        'base/servicos.html',
        {
            'servicos': servicos
        })


@login_required
def servico(request, id=False, situacao=False):

    servico_form = ServicoForm()

    if id:
        servico = Servico.objects.get(id=id)
        servico_form = ServicoForm(
            instance=servico, initial={
                'auto_complete_prefeitura': servico.prefeitura,
                'auto_complete_responsavel': servico.responsavel,
            })

    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)

        if id:
            servico_form = ServicoForm(
                request.POST, instance=servico, initial={
                    'auto_complete_prefeitura': servico.prefeitura,
                    'auto_complete_responsavel': servico.responsavel,
                })

        if servico_form.is_valid():
            servico = servico_form.save(commit=False)
            servico.status = True
            servico.save()
            messages.add_message(request, messages.SUCCESS, 'Serviço salvo com sucesso!')

            # send_mail(
            #     'Proposta Cadastrada',
            #     'Agiliza Convênios > Proposta cadastrada com sucesso',
            #     'sousa.tarcisio.s@gmail.com',
            #     ['tarcisio.sales@bol.com.br', ],
            #     fail_silently=False)

            return redirect(reverse('servicos'))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar o serviço!')

    return render(request, 'base/servico.html', {'servico_form': servico_form})


@login_required
def servico_excluir(request, id):
    servico = Servico.objects.get(id=id)
    servico.delete()
    messages.add_message(request, messages.INFO, 'Serviço excluído com sucesso!')
    return redirect(reverse('servicos'))


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

    if id:
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
    item_form = ItemForm(projeto)

    if (id):
        item = Item.objects.get(id=id)
        item_form = ItemForm(projeto, instance=item)

    if request.method == 'POST':

        item_form = ItemForm(projeto, request.POST)

        if id:
            item = Item.objects.get(id=id)
            item_form = ItemForm(projeto, request.POST, instance=item)

        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.projeto = projeto
            item.save()
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


def calcula_soma_valor_pagamento_convenente(execucoes_convenente):
    return sum([execucao_convenente.valor_pagamento for execucao_convenente in execucoes_convenente])


def calcula_percentual_convenente(execucoes_convenente):
    return sum([execucao_convenente.percentual for execucao_convenente in execucoes_convenente])


def calcula_soma_valor_pagamento_concedente(execucoes_concedente):
    return sum([execucao_concedente.valor_pagamento for execucao_concedente in execucoes_concedente])


def calcula_percentual_concedente(execucoes_concedente):
    return sum([execucao_concedente.percentual for execucao_concedente in execucoes_concedente])


@login_required
def protocolo(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    execucoes_convenente = ExecucaoConvenente.objects.filter(convenio=convenio)
    total_execucoes_convenentes = calcula_soma_valor_pagamento_convenente(execucoes_convenente)
    percentual_execucoes_convenentes = calcula_percentual_convenente(execucoes_convenente)
    execucoes_concedente = ExecucaoConcedente.objects.filter(convenio=convenio)
    total_execucoes_concedentes = calcula_soma_valor_pagamento_concedente(execucoes_concedente)
    percentual_execucoes_concedentes = calcula_percentual_concedente(execucoes_concedente)
    protocolos = Protocolo.objects.filter(convenio=convenio)

    proposta_form = PropostaValorLiberado(instance=convenio.proposta)
    if request.method == 'POST':
        proposta_form = PropostaValorLiberado(
            request.POST,
            instance=convenio.proposta
        )
        if proposta_form.is_valid():
            proposta = proposta_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Valor liberado R$ %s' % localize(proposta.valor_liberado)
            )
            return redirect(reverse('protocolo', args=[convenio.id]))

    return render(
        request,
        'base/protocolo.html',
        {
            'convenio': convenio,
            'execucoes_convenente': execucoes_convenente,
            'total_execucoes_convenentes': total_execucoes_convenentes,
            'percentual_execucoes_convenentes': percentual_execucoes_convenentes,
            'execucoes_concedente': execucoes_concedente,
            'total_execucoes_concedentes': total_execucoes_concedentes,
            'percentual_execucoes_concedentes': percentual_execucoes_concedentes,
            'protocolos': protocolos,
            'proposta_form': proposta_form,
        })


@login_required
def protocolos(request, convenio_id=False):
    convenio = Convenio.objects.get(id=convenio_id)
    protocolo_form = ProtocoloForm()
    if request.method == 'POST':
        protocolo_form = ProtocoloForm(request.POST, request.FILES)
        if protocolo_form.is_valid():
            protocolo = protocolo_form.save(commit=False)
            protocolo.convenio = convenio
            protocolo.save()
            return redirect(reverse('protocolo', args=[convenio.id]))

    return render(
        request,
        'base/protocolos.html',
        {
            'convenio': convenio,
            'protocolo_form': protocolo_form,
        })


@login_required
def protocolo_dados_bancarios(request, convenio_id):
    convenio = Convenio.objects.get(id=convenio_id)
    if convenio_id:
        protocolo_dados_bancarios_form = ProtocoloDadosBancariosForm(instance=convenio)
    if request.method == 'POST':
        if convenio_id:
            protocolo_dados_bancarios_form = ProtocoloDadosBancariosForm(request.POST, instance=convenio)

        if protocolo_dados_bancarios_form.is_valid():
            protocolo_dados_bancarios_form.save()
            messages.add_message(request, messages.SUCCESS, 'Dados bancários salvos com sucesso!')

            # send_mail(
            #     'Proposta Cadastrada',
            #     'Agiliza Convênios > Proposta cadastrada com sucesso',
            #     'sousa.tarcisio.s@gmail.com',
            #     ['tarcisio.sales@bol.com.br', ],
            #     fail_silently=False)

            return redirect(reverse('protocolo', args=[convenio.id]))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível salvar os dados bancários!')

    return render(request, 'base/protocolo_dados_bancarios.html', {
        'convenio': convenio,
        'protocolo_dados_bancarios_form': protocolo_dados_bancarios_form
    })


@login_required
def protocolo_empresa_contratada(request, convenio_id):
    convenio = Convenio.objects.get(id=convenio_id)
    if convenio_id:
        protocolo_empresa_contratada_form = ProtocoloEmpresaContratadaForm(instance=convenio)
    if request.method == 'POST':
        if convenio_id:
            protocolo_empresa_contratada_form = ProtocoloEmpresaContratadaForm(request.POST, instance=convenio)

        if protocolo_empresa_contratada_form.is_valid():
            protocolo_empresa_contratada_form.save()
            messages.add_message(request, messages.SUCCESS, 'Empresa contratada cadastrada com sucesso!')

            return redirect(reverse('protocolo', args=[convenio.id]))
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível cadastrar a empresa contratada!')

    return render(request, 'base/protocolo_empresa_contratada.html', {
        'convenio': convenio,
        'protocolo_empresa_contratada_form': protocolo_empresa_contratada_form
    })


@login_required
def protocolo_execucao_convenente(
        request,
        convenio_id,
        execucao_convenente_id=False):
    convenio = Convenio.objects.get(id=convenio_id)

    protocolo_execucao_convenente_form = ProtocoloExecucaoConvenenteForm()
    if execucao_convenente_id:
        execucao_convenente = ExecucaoConvenente.objects.get(
            id=execucao_convenente_id
        )
        protocolo_execucao_convenente_form = ProtocoloExecucaoConvenenteForm(
            instance=execucao_convenente
        )

    if request.method == 'POST':
        protocolo_execucao_convenente_form = ProtocoloExecucaoConvenenteForm(
            request.POST
        )
        if execucao_convenente_id:
            protocolo_execucao_convenente_form.instance = execucao_convenente

        if protocolo_execucao_convenente_form.is_valid():
            protocolo_execucao_convenente = protocolo_execucao_convenente_form.save(commit=False)
            protocolo_execucao_convenente.convenio = convenio
            protocolo_execucao_convenente.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Parcela cadastrada com sucesso!'
            )

            return redirect(reverse('protocolo', args=[convenio.id]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Não foi possível cadastrar a parcela!'
            )

    return render(request, 'base/protocolo_execucao_convenente.html', {
        'convenio': convenio,
        'protocolo_execucao_convenente_form': protocolo_execucao_convenente_form
    })


@login_required
def protocolo_execucao_convenente_excluir(request, id):
    execucao_convenente = ExecucaoConvenente.objects.get(id=id)
    execucao_convenente.delete()
    messages.add_message(request, messages.INFO, 'Pagamento excluído com sucesso!')
    return redirect(reverse('protocolo', args=[execucao_convenente.convenio.id]))


@login_required
def protocolo_execucao_concedente(
        request,
        convenio_id,
        execucao_concedente_id=False):
    convenio = Convenio.objects.get(id=convenio_id)

    protocolo_execucao_concedente_form = ProtocoloExecucaoConcedenteForm()
    if execucao_concedente_id:
        execucao_concedente = ExecucaoConcedente.objects.get(
            id=execucao_concedente_id
        )
        protocolo_execucao_concedente_form = ProtocoloExecucaoConcedenteForm(
            instance=execucao_concedente
        )

    if request.method == 'POST':
        protocolo_execucao_concedente_form = ProtocoloExecucaoConcedenteForm(
            request.POST
        )
        if execucao_concedente_id:
            protocolo_execucao_concedente_form.instance = execucao_concedente

        if protocolo_execucao_concedente_form.is_valid():
            protocolo_execucao_concedente = protocolo_execucao_concedente_form.save(commit=False)
            protocolo_execucao_concedente.convenio = convenio
            protocolo_execucao_concedente.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Parcela cadastrada com sucesso!'
            )

            return redirect(reverse('protocolo', args=[convenio.id]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Não foi possível cadastrar a parcela!'
            )

    return render(request, 'base/protocolo_execucao_concedente.html', {
        'convenio': convenio,
        'protocolo_execucao_concedente_form': protocolo_execucao_concedente_form
    })


@login_required
def protocolo_execucao_concedente_excluir(request, id):
    execucao_concedente = ExecucaoConcedente.objects.get(id=id)
    execucao_concedente.delete()
    messages.add_message(request, messages.INFO, 'Pagamento excluído com sucesso!')
    return redirect(reverse('protocolo', args=[execucao_concedente.convenio.id]))


@login_required
def protocolo_resolver(request, id):
    protocolo = Protocolo.objects.get(id=id)
    protocolo.situacao = 'resolvido'
    protocolo.save()
    return redirect(reverse('protocolo', args=[protocolo.convenio.id]))


@login_required
def protocolo_excluir(request, id):
    protocolo = Protocolo.objects.get(id=id)
    protocolo.delete()
    messages.add_message(request, messages.INFO, 'Protocolo excluído com sucesso!')
    return redirect(reverse('protocolo', args=[protocolo.convenio.id]))


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
def atividade_resolver(request, id):
    atividade = Atividade.objects.get(id=id)
    atividade.situacao = 'resolvido'
    atividade.save()
    return redirect(reverse('protocolo', args=[atividade.convenio.id]))


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


@login_required
def licenciamento_resolver(request, id):
    licenciamento = LicenciamentoAmbiental.objects.get(id=id)
    licenciamento.situacao = 'resolvido'
    licenciamento.save()
    return redirect(reverse('protocolo', args=[licenciamento.convenio.id]))

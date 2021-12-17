from django.db.models import Q
from django.views.generic.base import View
from core.base.models import Proposta, Convenio, Item, Prefeitura, ProjetoControle, ProjetoControleItem
from wkhtmltopdf.views import PDFTemplateResponse


class PropostasPDFView(View):
    template = 'reports/propostas.html'

    def get(self, request, filter_situacao=False):
        propostas = Proposta.objects.filter(status=True).order_by('-id')

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

        data = {'title': 'Propostas', 'propostas': propostas}

        response = PDFTemplateResponse(
            request=request,
            template=self.template,
            filename='propostas.pdf',
            context=data,
            show_content_in_browser=True,
            cmd_options={
                # 'margin-top': 10,
                # 'zoom': 1,
                'quiet': True,
                'enable-local-file-access': True,
                # 'viewport-size': '1366 x 513',
                # 'javascript-delay': 1000,
                'footer-center': '[page]/[topage]',
                # 'no-stop-slow-scripts': True
                },)

        return response


class ConveniosPDFView(View):
    template = 'reports/convenios.html'

    def get(self, request, filter_situacao=False):
        convenios = Convenio.objects.filter(status=True).order_by('-proposta__data')

        if not request.user.is_superuser and request.user.profissional.cargo.descricao == 'PREFEITO':
            prefeitura = Prefeitura.objects.get(prefeito=request.user.profissional)
            convenios = convenios.filter(proposta__prefeitura=prefeitura)

        if request.method == 'POST':
            if request.POST['search']:
                convenios = convenios.filter(
                    Q(numero=request.POST['search']) | Q(orgao=request.POST['search']))

        data = {'title': 'Convênios', 'convenios': convenios}

        response = PDFTemplateResponse(
            request=request,
            template=self.template,
            filename='convenios.pdf',
            context=data,
            show_content_in_browser=True,
            cmd_options={
                'margin-top': 10,
                'zoom': 1,
                'quiet': None,
                'enable-local-file-access': True,
                'viewport-size': '1366 x 513',
                'javascript-delay': 1000,
                'footer-center': '[page]/[topage]',
                'no-stop-slow-scripts': True},)

        return response


class ElaboracaoProjetoPDFView(View):
    template = 'reports/convenio_projeto_controle.html'

    def get(self, request, convenio_id=False):
        convenio = Convenio.objects.get(id=convenio_id)
        # projeto_controle_item_form = ProjetoControleItemForm()
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

        data = {
            'title': 'Elaboração de Projeto',
            'convenio': convenio,
            'controle': controle,
            'itens': itens
        }

        response = PDFTemplateResponse(
            request=request,
            template=self.template,
            filename='elaboracao_projeto.pdf',
            context=data,
            show_content_in_browser=True,
            cmd_options={
                'margin-top': 10,
                'zoom': 1,
                'quiet': None,
                'enable-local-file-access': True,
                'viewport-size': '1366 x 513',
                'javascript-delay': 1000,
                'footer-center': '[page]/[topage]',
                'no-stop-slow-scripts': True},)

        return response

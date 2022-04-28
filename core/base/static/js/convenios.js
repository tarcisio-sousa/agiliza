// const url_base = ''
const url_base = '/agiliza'
const url_projeto = 'projeto'
const url_convenio_aprovar_projeto = `convenio/aprovar/projeto`
const url_convenio_licitar_projeto = `convenio/licitar/projeto`
const url_convenio_analisar_licitacao = `convenio/analisar/licitacao`
const url_convenio_aprovar_licitacao = `convenio/aprovar/licitacao`
const url_convenio_recurso_conta = `convenio/recurso/em/conta`
const url_convenio_concluir = `convenio/concluir`
const url_concluir_prestacao_contas = `convenio/concluir/prestacao/contas`

let seleciona_convenio = (elemento) => {
    let form_convenio_projeto = document.getElementById('formConvenioProjeto')
    form_convenio_projeto.action =`${url_base}/${url_projeto}/${elemento.dataset.id}/`;
}

let aprovar_projeto_convenio = (elemento) => {
    let form_convenio_aprovar_projeto = document.getElementById('formAprovarProjeto')
    form_convenio_aprovar_projeto.action =`${url_base}/${url_convenio_aprovar_projeto}/${elemento.dataset.id}/`;
}

let licitar_projeto_convenio = (elemento) => {
    let form_convenio_licitar_projeto = document.getElementById('formLicitarProjeto')
    form_convenio_licitar_projeto.action =`${url_base}/${url_convenio_licitar_projeto}/${elemento.dataset.id}/`;
}

let analisar_licitacao_convenio = (elemento) => {
    let form_convenio_analisar_licitacao = document.getElementById('formAnalisarLicitacao')
    form_convenio_analisar_licitacao.action =`${url_base}/${url_convenio_analisar_licitacao}/${elemento.dataset.id}/`;
}

let aprovar_licitacao_convenio = (elemento) => {
    let form_convenio_aprovar_licitacao = document.getElementById('formAprovarLicitacao')
    form_convenio_aprovar_licitacao.action =`${url_base}/${url_convenio_aprovar_licitacao}/${elemento.dataset.id}/`;
}

let recurso_em_conta_convenio = (elemento) => {
    let form_convenio_recurso_conta = document.getElementById('formRecursoConta')
    form_convenio_recurso_conta.action =`${url_base}/${url_convenio_recurso_conta}/${elemento.dataset.id}/`;
}

let concluir_convenio = (elemento) => {
    let form_concluir_convenio = document.getElementById('formConcluirConvenio')
    form_concluir_convenio.action =`${url_base}/${url_convenio_concluir}/${elemento.dataset.id}/`;
}

let concluir_prestacao_contas = (elemento) => {
    let form_concluir_prestacao_contas = document.getElementById('formConcluirPrestacaoContas')
    form_concluir_prestacao_contas.action =`${url_base}/${url_concluir_prestacao_contas}/${elemento.dataset.id}/`;
}

let excluir_convenio = (item) => {
    alertify.confirm(
        'Tem certeza que deseja remover este convênio?',
        'Não será possível recuperar as informações deste registro',
        function() {
            console.log('Convênio excluído com sucesso')
            window.location.href = item.dataset.href
        },
        function() { console.log('Não foi possível excluir o convênio') })
        .set('labels', {ok: 'Sim, tenho certeza', cancel: 'Não'})
}

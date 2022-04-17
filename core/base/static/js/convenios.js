// const url_base = ''
const url_base = '/agiliza'
const url_projeto = 'projeto'

let seleciona_convenio = (elemento) => {
    let form_convenio_projeto = document.getElementById('formConvenioProjeto')
    form_convenio_projeto.action=`${url_base}/${url_projeto}/${elemento.dataset.id}/`;
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

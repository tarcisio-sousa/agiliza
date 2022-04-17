// const url_base = ''
const url_base = '/agiliza'

let excluir_servico = (item) => {
    alertify.confirm(
        'Tem certeza que deseja remover este serviço?',
        'Não será possível recuperar as informações deste registro',
        function() {
            console.log('Serviço excluído com sucesso')
            window.location.href = item.dataset.href
        },
        function() { console.log('Não foi possível excluir o serviço') })
        .set('labels', {ok: 'Sim, tenho certeza', cancel: 'Não'})
}

// const url_base = ''
const url_base = '/agiliza'

let excluir_protocolo = (item) => {
    alertify.confirm(
        'Tem certeza que deseja remover este registro?',
        'Não será possível recuperar as informações deste registro',
        function() {
            console.log('Registro excluído com sucesso')
            window.location.href = item.dataset.href
        },
        function() { console.log('Não foi possível excluir o registro') })
        .set('labels', {ok: 'Sim, tenho certeza', cancel: 'Não'})
}

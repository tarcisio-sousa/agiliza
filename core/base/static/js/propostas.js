// const url_base = ''
const url_base = '/agiliza'
// const url_api = '/api'
const url_api = '/agiliza/api'
const url_proposta_empenhar = `proposta/empenhar`
const url_proposta_arquivo_extrato = `proposta/arquivo/extrato`

const url_tecnico_orgao = 'tecnico/orgao'

let seleciona_empenhar_proposta = (elemento) => {
    let form_empenhar_proposta = document.getElementById('formEmpenharProposta')
    let input = document.getElementById("tecnico_orgao_nome")
    let telefoneTecnicoOrgao = document.getElementById("tecnico_orgao_telefone")
    let idTecnicoOrgao = document.getElementById("tecnico_orgao_id")

    form_empenhar_proposta.action = `${url_base}/${url_proposta_empenhar}/${elemento.dataset.id}/`

    autocomplete({
        input: input,
        minLength: 1,
        fetch: function(text, update) {
            load(true)
            text = text.toLowerCase();
            fetch(`${url_api}/${url_tecnico_orgao}/`, {
                method: 'GET'
            })
            .then(response => response.json())
            .then(data => {
                var suggestions = data.filter(n => n.nome.toLowerCase().startsWith(text))
                    .map(r => { return { 'label': r.nome, 'value': r.id, 'telefone': r.telefone }})
                update(suggestions);
            })
            .catch(error => console.log('Error: ', error))
            .finally(() => {
                load(false)
            })
        },
        onSelect: function(item) {
            input.value = item.label;
            idTecnicoOrgao.value = item.value;
            telefoneTecnicoOrgao.value = item.telefone;
        },
        debounceWaitMs: 300,
    });
}

let seleciona_proposta_arquivo_extrato = (elemento) => {
    let form_extrato = document.getElementById('formExtrato')
    form_extrato.action = `${url_base}/${url_proposta_arquivo_extrato}/${elemento.dataset.id}/`
}

let aprovar_proposta = (item) => {
    alertify.confirm(
        'Aprovar proposta',
        'Tem certeza que deseja aprovar esta proposta?',
        function() {
            window.location.href = item.dataset.href
        },
        function() { console.log('Não foi possível reprovar o item') })
        .set('labels', {ok: 'Sim', cancel: 'Não'})
}


let reprovar_proposta = (item) => {
    alertify.confirm(
        'Reprovar proposta',
        'Tem certeza que deseja reprovar esta proposta?',
        function() {
            window.location.href = item.dataset.href
        },
        function() { console.log('Não foi possível reprovar o item') })
        .set('labels', {ok: 'Sim', cancel: 'Não'})
}

let excluir_proposta = (item) => {
    alertify.confirm(
        'Tem certeza que deseja remover esta proposta?',
        'Não será possível recuperar as informações deste registro',
        function() {
            console.log('Proposta excluída com sucesso')
            window.location.href = item.dataset.href
        },
        function() { console.log('Não foi possível excluir o item') })
        .set('labels', {ok: 'Sim, tenho certeza', cancel: 'Não'})
}

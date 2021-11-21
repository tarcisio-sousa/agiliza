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
        fetch: function(text, update) {
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

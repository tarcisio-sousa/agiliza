const url_base = ''
// const url_base = '/agiliza'
const url_proposta_empenhar = `proposta/empenhar`
const url_proposta_arquivo_extrato = `proposta/arquivo/extrato`

let seleciona_empenhar_proposta = (elemento) => {
    let form_empenhar_proposta = document.getElementById('formEmpenharProposta')
    form_empenhar_proposta.action = `${url_base}/${url_proposta_empenhar}/${elemento.dataset.id}/`
}

let seleciona_proposta_arquivo_extrato = (elemento) => {
    let form_extrato = document.getElementById('formExtrato')
    form_extrato.action = `${url_base}/${url_proposta_arquivo_extrato}/${elemento.dataset.id}/`
}

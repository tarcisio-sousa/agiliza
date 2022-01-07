// const url_base = ''
const url_base = '/agiliza'
// const url_api = '/api'
const url_api = '/agiliza/api'

const url_prefeituras = 'prefeituras'

let input_prefeitura = document.getElementById("id_auto_complete_prefeitura")
let idPrefeitura = document.getElementById("id_prefeitura")

const url_responsaveis = 'responsaveis'

let input_responsavel = document.getElementById("id_auto_complete_responsavel")
let idResponsavel = document.getElementById("id_responsavel")

autocomplete({
    input: input_prefeitura,
    minLength: 1,
    fetch: function(text, update) {
        load(true)
        text = text.toLowerCase();
        fetch(`${url_api}/${url_prefeituras}/`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => {
            var suggestions = data.filter(n => n.nome.toLowerCase().startsWith(text))
                .map(r => { return { 'label': r.nome, 'value': r.id }})
            update(suggestions);
        })
        .catch(error => console.log('Error: ', error))
        .finally(() => {
            load(false)
        })
    },
    onSelect: function(item) {
        input_prefeitura.value = item.label;
        idPrefeitura.value = item.value;
    },
    debounceWaitMs: 300,
    emptyMsg: "Prefeitura não encontrada",
});

autocomplete({
    input: input_responsavel,
    minLength: 1,
    fetch: function(text, update) {
        load(true)
        text = text.toLowerCase();
        fetch(`${url_api}/${url_responsaveis}/`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => {
            var suggestions = data.filter(n => n.nome.toLowerCase().startsWith(text))
                .map(r => { return { 'label': r.nome, 'value': r.id }})
            update(suggestions);
        })
        .catch(error => console.log('Error: ', error))
        .finally(() => {
            load(false)
        })
    },
    onSelect: function(item) {
        input_responsavel.value = item.label;
        idResponsavel.value = item.value;
    },
    debounceWaitMs: 300,
    emptyMsg: "Responsável não encontrado",
});
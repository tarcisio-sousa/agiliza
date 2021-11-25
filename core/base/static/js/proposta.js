// const url_base = ''
const url_base = '/agiliza'
// const url_api = '/api'
const url_api = '/agiliza/api'

const url_prefeituras = 'prefeituras'

let input = document.getElementById("id_auto_complete_prefeitura")
let idPrefeitura = document.getElementById("id_prefeitura")

autocomplete({
    input: input,
    minLength: 1,
    fetch: function(text, update) {
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
    },
    onSelect: function(item) {
        input.value = item.label;
        idPrefeitura.value = item.value;
    },
    debounceWaitMs: 300,
    emptyMsg: "Prefeitura não encontrada",
});
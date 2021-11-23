// const url_api = '/api'
const url_api = '/agiliza/api'
const url_item_controle = 'item/controle'

const token = document.querySelector('[name=csrfmiddlewaretoken]').value

let abrirItemModal = (el) => {
    let posicao = pegarPosicaoItem(el)
    $('#itemModal').modal('show')
    document.getElementById('itemControleForm').reset();
    document.getElementById('itemControleForm').dataset.posicao = posicao
    if (el.dataset.id != 'False') {
        document.getElementById('itemControleForm').dataset.id = el.dataset.id
        apiCarregarFormularioItemControle(el.dataset.id)
    }
    document.getElementById('id_item').value = el.dataset.itemId
}


let submeterItemControle = (formulario) => {
    event.preventDefault()
    let posicao = formulario.dataset.posicao
    let id = formulario.dataset.id || false
    dados = new FormData(formulario)
    apiSubmeterDadosItemControle(dados, id, posicao)
}

let removerItemControle = (el) => {
    let id = el.dataset.id
    let item = el.dataset.itemId
    let posicao = el.dataset.posicao
    alertify.confirm(
        'Remover item', 
        'Tem certeza que deseja remover este item?', 
        function() { 
            apiDeletarItemControle(id, item, posicao)
        },
        function() { console.log('Não foi possível remover o item') })
        .set('labels', {ok: 'Sim', cancel: 'Não'})
}

function pegarMetodoSubmeter(id) {
    if (id) return { url: `${url_api}/${url_item_controle}/${id}/`, method: 'PUT' }
    return { url: `${url_api}/${url_item_controle}/`, method: 'POST' }
}

let apiSubmeterDadosItemControle = (dados, id, posicao = false) => {
    let requisicao = pegarMetodoSubmeter(id)

    fetch(requisicao.url, {
        method: requisicao.method,
        headers: {
            'X-CSRFToken': token
        },
        body: dados
    })
    .then(response => response.json())
    .then(data => {
        apiCarregarDadosItemControle(data.id, posicao)
        fecharItemModal()
    })
    .catch(error => console.log('Error: ', error)) }

let apiCarregarDadosItemControle = (id, posicao = false) => {
    fetch(`${url_api}/${url_item_controle}/${id}/`, {
        method: 'GET',
        headers: {
            'X-CSRFToken': token
        }
    })
    .then(response => response.json())
    .then(data => {
        carregarItemControle(data, posicao)
    })
    .catch(error => console.log('Error: ', error)) }

let apiCarregarFormularioItemControle = (id) => {
    fetch(`${url_api}/${url_item_controle}/${id}/`, {
        method: 'GET',
        headers: {
            'X-CSRFToken': token
        }
    })
    .then(response => response.json())
    .then(data => {
        carregarFormularioItemControle(data)
    })
    .catch(error => console.log('Error: ', error)) }

let carregarFormularioItemControle = (item) => {
    document.getElementById('id_alternativa').value = item.alternativa.id
    document.getElementById('id_data_prevista').value = formatarData(item.data_prevista)
    document.getElementById('id_responsavel').value = item.responsavel.id
    document.getElementById('id_observacoes').value = item.observacoes
    document.getElementById('id_comentario').value = item.comentario
}

let carregarItemControle = (item, posicao = false) => {
    let alternativa = document.getElementsByClassName('alternativa')[posicao]
    let observacoes = document.getElementsByClassName('observacoes')[posicao]
    let responsavel = document.getElementsByClassName('responsavel')[posicao]
    let data_prevista = document.getElementsByClassName('data_prevista')[posicao]
    let remover = document.getElementsByClassName('remover')[posicao]
    let submeter = document.getElementsByClassName('botao_submeter_item_controle')[posicao]
    alternativa.innerHTML = item.alternativa.descricao
    observacoes.innerHTML = item.observacoes
    responsavel.innerHTML = (item.responsavel) ? item.responsavel.nome : ''
    data_prevista.innerHTML = formatarData(item.data_prevista)
    remover.innerHTML = `<a href='javascript: void(0);' onclick='removerItemControle(this)' data-posicao='${posicao}' data-item-id='${item.item}' data-id='${item.id}' class='btn btn-sm btn-link text-danger'><i class='fas fa-times-circle'></i></a>`
    submeter.dataset.id = item.id
}

let deletarItemControle = (id, item, posicao = false) => {
    let alternativa = document.getElementsByClassName('alternativa')[posicao]
    let observacoes = document.getElementsByClassName('observacoes')[posicao]
    let responsavel = document.getElementsByClassName('responsavel')[posicao]
    let data_prevista = document.getElementsByClassName('data_prevista')[posicao]
    let remover = document.getElementsByClassName('remover')[posicao]
    let submeter = document.getElementsByClassName('botao_submeter_item_controle')[posicao]
    alternativa.innerHTML = ''
    observacoes.innerHTML = ''
    responsavel.innerHTML = ''
    data_prevista.innerHTML = ''
    remover.innerHTML = ''
    submeter.dataset.id = 'False'
}

let apiDeletarItemControle = (id, item, posicao = false) => {
    fetch(`${url_api}/${url_item_controle}/${id}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': token
        }
    })
    .then(response => console.log(response))
    .then(data => {
        deletarItemControle(id, item, posicao)
    })
    .catch(error => console.log('Error: ', error)) }

let fecharItemModal = () => {
    $('#itemModal').modal('hide')
}

function pegarPosicaoItem(item) {
    var lista = document.getElementsByClassName('botao_submeter_item_controle')
    lista = [].slice.call(lista)
    posicao = lista.indexOf(item)
    return posicao
}

function formatarData(data) {
    if (data) { 
        elemento = data.split('-')
        data = [elemento[2], elemento[1], elemento[0]]
        data = data.join('/')
    }
    return data
}

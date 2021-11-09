const url_base = ''
// const url_base = '/agiliza'
const url_projeto = 'projeto'

let seleciona_convenio = (elemento) => {
    let form_convenio_projeto = document.getElementById('formConvenioProjeto')
    form_convenio_projeto.action=`${url_base}/${url_projeto}/${elemento.dataset.id}/`;
}

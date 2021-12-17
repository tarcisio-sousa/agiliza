// vanillajs 
window.onload = function(){
    const btn_sair = document.getElementById('btn-sair-agiliza');
    const sair = btn_sair.getElementsByTagName('i')[0];
    let handler = event => {
        if (event.type == 'mouseover') { 
            sair.classList.remove('fa-door-closed')
            sair.classList.add('fa-door-open')
        }
        if (event.type == 'mouseleave') { 
            sair.classList.add('fa-door-closed')
            sair.classList.remove('fa-door-open')
        }
    }
    
    btn_sair.onmouseover = btn_sair.onmouseleave = handler

}

let load = run => {
    run ? loading() : ready()
}

let loading = _ => {
    console.log('Carregando...')
    document.querySelectorAll('.lds-ring').forEach((item, id) => {
        item.classList.remove('d-none')
    })
}

let ready = _ => {
    console.log('Pronto...')
    document.querySelectorAll('.lds-ring').forEach((item, id) => {
        item.classList.add('d-none')
    })
}

// libs 
alertify.defaults = {
    // dialogs defaults
    autoReset:true,
    basic:false,
    closable:true,
    closableByDimmer:true,
    invokeOnCloseOff:false,
    frameless:false,
    defaultFocusOff:false,
    maintainFocus:true, // <== global default not per instance, applies to all dialogs
    maximizable:true,
    modal:true,
    movable:true,
    moveBounded:false,
    overflow:true,
    padding: true,
    pinnable:true,
    pinned:true,
    preventBodyShift:false, // <== global default not per instance, applies to all dialogs
    resizable:true,
    startMaximized:false,
    transition:'pulse',
    transitionOff:false,
    tabbable:'button:not(:disabled):not(.ajs-reset),[href]:not(:disabled):not(.ajs-reset),input:not(:disabled):not(.ajs-reset),select:not(:disabled):not(.ajs-reset),textarea:not(:disabled):not(.ajs-reset),[tabindex]:not([tabindex^="-"]):not(:disabled):not(.ajs-reset)',  // <== global default not per instance, applies to all dialogs

    // notifier defaults
    notifier:{
    // auto-dismiss wait time (in seconds)  
        delay:5,
    // default position
        position:'bottom-right',
    // adds a close button to notifier messages
        closeButton: false,
    // provides the ability to rename notifier classes
        classes : {
            base: 'alertify-notifier',
            prefix:'ajs-',
            message: 'ajs-message',
            top: 'ajs-top',
            right: 'ajs-right',
            bottom: 'ajs-bottom',
            left: 'ajs-left',
            center: 'ajs-center',
            visible: 'ajs-visible',
            hidden: 'ajs-hidden',
            close: 'ajs-close'
        }
    },

    // language resources 
    glossary:{
        // dialogs default title
        title:'Alerta',
        // ok button text
        ok: 'OK',
        // cancel button text
        cancel: 'Cancel'            
    },

    // theme settings
    theme:{
        // class name attached to prompt dialog input textbox.
        input:'ajs-input', // -- default
        // input:'ui positive button', // -- semantic
        // class name attached to ok button
        ok:'ajs-ok', // -- default
        // ok:'ui positive button', // -- semantic
        // class name attached to cancel button 
        cancel:'ajs-cancel' // -- default 
        // cancel:'ui black button' // -- semantic
    },
    // global hooks
    hooks:{
        // invoked before initializing any dialog
        preinit:function(instance){},
        // invoked after initializing any dialog
        postinit:function(instance){},
    },
};

alertify.defaults.theme.ok = "btn btn-sm btn-primary";
alertify.defaults.theme.cancel = "btn btn-sm btn-secondary";
alertify.defaults.theme.input = "form-control";


// JQuery
$(function () {
    $.datetimepicker.setLocale('pt-BR')
    $('.date').datetimepicker({
        format: 'd/m/Y',
        timepicker: false,
        mask: true,
    })
    $('.money').maskMoney({thousands:'.', decimal:',', allowZero: true})
})


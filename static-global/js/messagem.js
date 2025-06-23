var mensagem = {};

(function(context) {
    const cores = {
        'error': "#F56565",
        'success': "#48BB78"
    }
    context.criar = (tipo, texto) => {
        Toastify({
            text: texto,
            duration: 3000,
            newWindow: true,
            close: true,
            gravity: "top",
            position: "right",
            stopOnFocus: true,
            style: {
            background: cores[tipo],
            },
            onClick: function(){}
        }).showToast();
    }
})(mensagem);
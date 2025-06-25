const questionForm = document.querySelector('#answer-form');
const url = questionForm.getAttribute("action")

questionForm.addEventListener('submit', async function (event) {
    event.preventDefault();
    const outputData = await editor.save();

    const formData = new FormData();

    formData.append('content', JSON.stringify(outputData));
    formData.append('questionId', questionForm.elements.questionId.value);

    const response = await fetch(url, {
        method: 'POST',
        headers: {

            'X-CSRFToken': csrfToken,
            'Accept': 'application/json'
        },
        body: formData,
    });

    if (!response.ok || (outputData.blocks.length === 0)) {
        Toastify({
            text: "Erro ao criar pergunta! Por favor, verifique os campos e tente novamente.", // Mensagem mais clara e orientada à ação
            duration: 2000, // Aumenta a duração para o usuário ter mais tempo para ler
            close: true, // Permite fechar o toast manualmente
            gravity: "top", // Posição superior
            position: "center", // Centraliza o toast para maior visibilidade
            stopOnFocus: true, // Mantém o toast visível se o usuário interagir com ele
            style: {
                background: "#FF5733",
                borderRadius: '2rem'
            },
        }).showToast();
    } else {
        Toastify({
            text: "Resposta criada com sucesso! Você será redirecionado em breve.",
            duration: 1000,
            close: true,
            gravity: "top",
            position: "center",
            stopOnFocus: true,
            style: {
                background: "#008577",
                borderRadius: '2rem',
                boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)'
            },
            callback: function () {
                window.location.reload();
            }
        }).showToast();
    }

});

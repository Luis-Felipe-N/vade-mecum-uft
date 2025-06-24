const btnsVote = document.querySelectorAll(".vote-btn")
const csrfTokenForm = document.querySelector("#csrf-token-form")
const csrfToken = csrfTokenForm.elements.csrfmiddlewaretoken.value

async function handleClickBtnVote(evt) {
    const url = evt.target.getAttribute('vote-answer-url')

    console.log({ csrfToken, url })

    const response = await fetch(url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
    });

    if (!response.ok) {
        throw new Error(`Erro ao buscar dados das atividades: ${response.statusText}`);
    }
    return await response.json();
}

for (const btnVote of btnsVote) {
    btnVote.addEventListener('click', handleClickBtnVote)
}


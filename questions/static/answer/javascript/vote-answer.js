const btnsVote = document.querySelectorAll(".vote-btn")
const csrfTokenForm = document.querySelector("#csrf-token-form")
const csrfToken = csrfTokenForm.elements.csrfmiddlewaretoken.value

async function handleClickBtnVote(evt) {
    // const dataTYPE = {
    //     "answer_id": 43,
    //     "best_answer_has_change": false,
    //     "message": "Seu voto foi removido/Seu voto foi registrado",
    //     "new_score": 0,
    //     "status": "success"
    // }

    const url = evt.target.getAttribute('vote-answer-url')

    evt.target.innerHTML = `
        <span>
            <i class="fa-solid fa-heart"></i></span>
            Obrigado
            <div class="spinner-border" role="status" style="height: 17px;width: 17px;">
                <span class="visually-hidden">Loading...</span>
            </div>
    `

    setTimeout(async () => {
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

        const data = await response.json();

        evt.target.innerHTML = `
            <span>
                <i class="fa-solid fa-heart"></i></span>
                Obrigado
                ${data.new_score}
        `

        if (data.best_answer_has_change) {
            location.reload()
        }
    }, 500)
}

for (const btnVote of btnsVote) {
    btnVote.addEventListener('click', handleClickBtnVote)
}


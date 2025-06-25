const file = document.querySelector("#id_file_attachment")
const btnFile = document.querySelector(".btn-file")
file.onchange = (evt) => {
    const attach = evt.target.files

    if (attach.length > 0) {
        btnFile.classList.add('d-none')
        const preview = attach.files[0]

        document.querySelector("#preview_file_attachment").innerHTML = `
                <div style="display: inline-flex;" class="bg-light p-2 align-items-center gap-2" >
                <embed class="rounded" type="image/jpg" src="http://127.0.0.1:8000/vademecum/media/profile_pics/ChatGPT_Image_Jun_16_2025_10_47_46_AM.png" width="30" height="30">

                <strong>imagem.png</strong>
                <button type="button" class="btn p-0"><i class=" fa-solid fa-xmark btn-close"></i></button>
            </div>
        `

        document.querySelector('.btn-close').onclick = () => {
            evt.target.files = []
        }
    } else {
        btnFile.classList.add('d-flex')
    }
}
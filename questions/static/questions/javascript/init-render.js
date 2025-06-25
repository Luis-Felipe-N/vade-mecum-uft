const contents = document.querySelectorAll('.editorjs-output')

console.log(contents)

for (const content of contents) {
    const editorJsData = JSON.parse(content.textContent)
    const outputContainer = document.getElementById('');

    if (typeof editorJsData === 'object' && editorJsData !== null && Array.isArray(editorJsData.blocks)) {
        const editorJsHtml = edjsHTML();

        const html = convertDataToHtml(editorJsData.blocks);
        console.log(html)
        content.innerHTML = html
    } else {
        console.error("Dados do Editor.js inválidos ou ausentes.");
        outputContainer.textContent = "Conteúdo não disponível.";
    }
}

function convertDataToHtml(blocks) {
    console.log(blocks)
    var convertedHtml = "";
    blocks.map(block => {

        switch (block.type.toLowerCase()) {
            case "header":
                convertedHtml += `<h${block.data.level}>${block.data.text}</h${block.data.level}>`;
                break;
            case "embded":
                convertedHtml += `<div><iframe width="560" height="315" src="${block.data.embed}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>`;
                break;
            case "paragraph":
                convertedHtml += `<p>${block.data.text}</p>`;
                break;
            case "delimiter":
                convertedHtml += "<hr />";
                break;
            case "image":
                convertedHtml += `<img class="img-fluid" src="${block.data.file.url}" title="${block.data.caption}" /><br /><em>${block.data.caption}</em>`;
                break;
            case "list":
                convertedHtml += "<ul>";
                block.data.items.forEach(function (li) {
                    convertedHtml += `<li>${li.content}</li>`;
                });
                convertedHtml += "</ul>";
                break;
            default:
                console.log("Unknown block type", block.type);
                break;
        }
    });
    return convertedHtml;
}
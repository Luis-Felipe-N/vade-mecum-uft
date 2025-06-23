document.querySelectorAll('.selectchoice').forEach(element => {
    const choices = new Choices(element, {
        removeItems: true,
        removeItemButton: true,
        loadingText: 'Pesquisando...',
        noResultsText: 'Nenhum resultado encontrado',
        noChoicesText: 'Sem opções para escolha',
        itemSelectText: 'Clique para selecionar',
        uniqueItemText: 'Permitido apenas uma escolha',
        customAddItemText: 'Somente valores correspondentes a condições específicas podem ser adicionados',
        addItemText: (value) => {
            return `Clique para adicionar <b>"${value}"</b>`;
        },
        maxItemText: (maxItemCount) => {
            return `Apenas ${maxItemCount} itens pode ser adicionados`;
        },
    })
})

document.querySelectorAll('.selectchoicemultiple').forEach(element => {
    const choices = new Choices(element, {
        removeItems: true,
        removeItemButton: true,
        loadingText: 'Pesquisando...',
        noResultsText: 'Nenhum resultado encontrado',
        noChoicesText: 'Sem opções para escolha',
        itemSelectText: 'Clique para selecionar',
        uniqueItemText: 'Permitido apenas uma escolha',
        customAddItemText: 'Somente valores correspondentes a condições específicas podem ser adicionados',
        addItemText: (value) => {
            return `Clique para adicionar <b>"${value}"</b>`;
        },
        maxItemText: (maxItemCount) => {
            return `Apenas ${maxItemCount} itens pode ser adicionados`;
        },
    })
})


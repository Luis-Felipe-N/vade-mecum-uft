const editor = new EditorJS({
    holder: 'editorjs',
    placeholder: 'Como configurar um banco de dados SQL?',
    tools: {
        header: {
            class: Header,
            inlineToolbar: ['link'],
            config: {
                placeholder: 'Título'
            },
            levels: [1, 2, 3, 4],
            defaultLevel: 2
        },
        code: CodeTool,
        List: {
            class: EditorjsList,
            inlineToolbar: true,
            config: {
                defaultStyle: 'unordered'
            },
        },
    }
});
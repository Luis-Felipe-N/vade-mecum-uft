# questions/forms.py
from django import forms
from questions.models import Question

class QuestionForm(forms.ModelForm):
    content = forms.CharField(widget=forms.HiddenInput(), required=True)
    # content = forms.CharField(widget=forms.Textarea(attrs={'id': 'editorjs-content-area'}), required=True)

    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título da sua pergunta'}),
        }

    def clean_content(self):
        content_data = self.cleaned_data['content']
        if not content_data:
            raise forms.ValidationError("O conteúdo da pergunta não pode ser vazio.")
        import json
        try:
            json.loads(content_data)
        except json.JSONDecodeError:
            raise forms.ValidationError("Formato de conteúdo inválido.")
        return content_data
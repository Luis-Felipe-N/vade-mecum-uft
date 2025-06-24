from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from cadastro.models import Person 
from questions.models import Subject 

User = get_user_model()

class UserAndPersonCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="E-mail",
        required=True,
        help_text="Obrigatório. Digite um e-mail válido para login."
    )

    full_name = forms.CharField(
        max_length=200,
        label="Nome Completo",
        help_text="Seu nome completo."
    )
    birth_date = forms.DateField(
        label="Data de Nascimento",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Sua data de nascimento."
    )
    gender = forms.ChoiceField(
        choices=Person.GENDER_CHOICES,
        label="Gênero",
        required=False
    )
    enrollment_number = forms.CharField(
        max_length=50,
        label="Número de Matrícula (UFT)",
        required=False,
        help_text="Seu número de matrícula na UFT (opcional)."
    )

    enrolled_subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        label="Disciplinas Cursadas",
        required=False,
        help_text="Selecione as disciplinas que você cursou ou está cursando."
    )
    
    bio = forms.CharField(
        widget=forms.Textarea,
        label="Biografia",
        required=False,
        help_text="Uma breve descrição sobre você."
    )
    profile_picture = forms.ImageField(
        label="Foto de Perfil",
        required=False,
        help_text="Faça upload de uma foto para o seu perfil."
    )

    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ('username', 'email', ) + UserCreationForm.Meta.fields 


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False) 
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        person_profile = Person(user=user)
        person_profile.full_name = self.cleaned_data['full_name']
        person_profile.birth_date = self.cleaned_data['birth_date']
        person_profile.gender = self.cleaned_data['gender']
        person_profile.enrollment_number = self.cleaned_data['enrollment_number']
        person_profile.bio = self.cleaned_data['bio']
        person_profile.profile_picture = self.cleaned_data['profile_picture']
        
        if commit:
            person_profile.save()
            if 'enrolled_subjects' in self.cleaned_data and self.cleaned_data['enrolled_subjects']:
                person_profile.enrolled_subjects.set(self.cleaned_data['enrolled_subjects'])
            
        return user 
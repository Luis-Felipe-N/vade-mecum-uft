from localflavor.br.forms import BRCPFField
from django.forms import ModelForm
from django import forms

############
from cadastro.models import Pessoa

class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Pessoa
        fields=('username','password')
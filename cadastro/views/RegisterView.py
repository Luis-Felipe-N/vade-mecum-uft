from django.contrib.auth import get_user_model, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured

from cadastro.forms import UserAndPersonCreationForm

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel 
    success_url = reverse_lazy('indexSistema')
    form_class = UserAndPersonCreationForm
    template_name = 'auth/register-view.html'

    def dispatch(self, request, *args, **kwargs):
        self.nextPage = self.request.GET.get("next", "")
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        user = form.save() 
        
        login(self.request, user)

        messages.success(self.request, "Cadastro realizado com sucesso!")
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.nextPage:
            return f'{str(self.success_url)}?next={self.nextPage}'
        return str(self.success_url)
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import  RedirectView

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('cadastro:login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
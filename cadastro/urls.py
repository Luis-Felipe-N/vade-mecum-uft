from django.urls import path

from cadastro.views import LoginView, LogoutView, RegisterView
app_name = 'cadastro'

urlpatterns = [
    path('singin/', LoginView.as_view(), name='login'),
    path('singup/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
#   path('perfil/', PerfilView.as_view(), name='perfil'),
#   path('avnei/confirmacao/<int:pk>', ConfirmacaoEmailView.as_view(), name='confirmacao-conta'),    
  
#   path('avnei/aterarseanha/automatica/<int:pk>', AlterarSenhaAutomaticamenteView.as_view(), name='alterar-senha-automatica'),    
#   path('avnei/aterarseanha/padrao/<int:pk>', AlterarSenhaPadraoView.as_view(), name='alterar-senha-padrao'),    
]


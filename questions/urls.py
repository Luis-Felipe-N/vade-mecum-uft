from django.urls import path

from questions.views import QuestionsListView

urlpatterns = [
    path('', QuestionsListView.as_view(), name='indexSistema'),
    # path('logout/', views.CustomLogoutView.as_view(), name='logout'),
#   path('perfil/', PerfilView.as_view(), name='perfil'),
#   path('avnei/confirmacao/<int:pk>', ConfirmacaoEmailView.as_view(), name='confirmacao-conta'),    
  
#   path('avnei/aterarseanha/automatica/<int:pk>', AlterarSenhaAutomaticamenteView.as_view(), name='alterar-senha-automatica'),    
#   path('avnei/aterarseanha/padrao/<int:pk>', AlterarSenhaPadraoView.as_view(), name='alterar-senha-padrao'),    
]



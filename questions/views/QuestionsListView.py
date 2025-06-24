from django.views.generic import ListView
#########################################
from questions.models import Question


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/list-questions.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user.person_profile)
        return context
    
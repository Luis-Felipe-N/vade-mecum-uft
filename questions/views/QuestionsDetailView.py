from django.views.generic import DetailView
#########################################
from questions.models import Question


class QuestionsDetailView(DetailView):
    model = Question
    template_name = 'questions/detail-question.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user.person_profile)
        return context
    
from django.views.generic import ListView
#########################################
from questions.models import Question


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/list-questions.html'
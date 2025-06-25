from django.views.generic import ListView
from django.db.models import Q
#########################################
from questions.models import Question, Subject
from questions.form import QuestionForm

class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/list-questions.html'
    
    def get_queryset(self):
        query = super().get_queryset()
        
        term = self.request.GET.get('q')
        
        if term:
            query = query.filter(Q(Q(title__icontains=term) | Q(content__icontains=term)))
        
        return query
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        context["form"] = QuestionForm()
        return context
    
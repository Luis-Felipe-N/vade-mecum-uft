from rest_framework.views import APIView
from questions.models import Question
from api.serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class QuestionAPIView(APIView):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
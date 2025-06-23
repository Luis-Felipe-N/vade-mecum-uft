from rest_framework.views import APIView
from questions.models import Answer
from api.serializers import AnswerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AnswerViewSet(APIView):
    queryset = Answer.objects.all().order_by('data_criacao')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
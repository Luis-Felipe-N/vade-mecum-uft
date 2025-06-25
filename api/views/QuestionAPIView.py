from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser 

from questions.models import Question
from cadastro.models import Person
from api.serializers import QuestionSerializer

class QuestionAPIView(APIView):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated] 
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            author = Person.objects.get(user=request.user)
            question = serializer.save(author=author)

            return Response(
                {
                    "status": "success",
                    "message": "Pergunta criada com sucesso!",
                    "question_id": question.id,
                    "data": serializer.data,
                    "get_absolute_url": question.get_absolute_url()
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

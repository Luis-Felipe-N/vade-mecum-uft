from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser 

from questions.models import Answer, Question
from api.serializers import AnswerSerializer
from cadastro.models import Person

class AnswerAPIView(APIView):
    queryset = Answer.objects.all().order_by('created_at')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated] 
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            question = Question.objects.get(pk=request.data.get('questionId'))
            author = Person.objects.get(user=request.user)
            answer = serializer.save(author=author, question=question)

            return Response(
                {
                    "status": "success",
                    "message": "Pergunta criada com sucesso!",
                    "answer_id": answer.id,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from questions.models import Answer, Vote 
from cadastro.models import Person
from api.serializers import VoteSerializer 

class VoteAnswerAPIView(APIView):
    queryset = Vote.objects.all().order_by('created_at')
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def post(self, request, answer_id, vote_type, format=None):
        answer = None
        
        try:
            answer = Answer.objects.get(pk=answer_id)
        except Answer.DoesNotExist:
            return Response(
                {"detail": "Resposta não encontrada."},
                status=status.HTTP_404_NOT_FOUND
            )

        user = request.user
        if not user.is_authenticated:
            return Response(
                {"detail": "Autenticação necessária para votar."},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        person = Person.objects.get(user=user)

        if vote_type.lower() == 'upvote':
            vote_value = Vote.UPVOTE
        elif vote_type.lower() == 'downvote':
            vote_value = Vote.DOWNVOTE
        else:
            return Response(
                {"detail": "Tipo de voto inválido. Use 'upvote' ou 'downvote'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        existing_vote = Vote.objects.filter(author=person, answer=answer).first()

        if existing_vote:
            if existing_vote.vote_type == vote_value:
                existing_vote.delete()
                message = "Seu voto foi removido."
            else:
                existing_vote.vote_type = vote_value
                existing_vote.save()
                message = "Seu voto foi atualizado."
        else:
            Vote.objects.create(author=person, answer=answer, vote_type=vote_value)
            message = "Seu voto foi registrado."
        
        updated_score = answer.total_votes
        
        best_answer = answer.question.answers.filter(is_best_answer=True)
        print(best_answer)
        if best_answer.exists():
            print(best_answer.get().total_votes, updated_score)
            if best_answer.get().total_votes < updated_score:
                best_answer.get().is_best_answer = False
                answer.is_best_answer = True
                best_answer.get().save()
        else:
            answer.is_best_answer = True

        answer.save()
        
        return Response(
            {
                "status": "success",
                "message": message,
                "answer_id": answer.id,
                "new_score": updated_score
            },
            status=status.HTTP_200_OK
        )

 
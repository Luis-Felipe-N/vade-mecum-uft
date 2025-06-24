# questions/models.py
from django.db import models
from django.conf import settings # Para pegar o AUTH_USER_MODEL
from django.utils import timezone
#################################
from questions.models import Answer
from cadastro.models import Person

class Vote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )
    
    author = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='votes',
        verbose_name="Usuário"
    )

    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='votes',
        verbose_name="Resposta"
    )
    
    vote_type = models.SmallIntegerField(
        choices=VOTE_CHOICES,
        verbose_name="Tipo de Voto"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        unique_together = ('author', 'answer')
        verbose_name = "Voto"
        verbose_name_plural = "Votos"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author.full_name} {self.get_vote_type_display()} em '{self.answer.content[:30]}...'"
    

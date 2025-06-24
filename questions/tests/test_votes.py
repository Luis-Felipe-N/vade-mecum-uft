# questions/tests/test_votes.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from questions.models import Question, Answer, Vote 
from cadastro.models import Person

User = get_user_model()

class VoteModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', email='user1@example.com', password='password123')
        self.user2 = User.objects.create_user(username='testuser2', email='user2@example.com', password='password123')
        self.user3 = User.objects.create_user(username='testuser3', email='user3@example.com', password='password123')

        self.person1 = Person.objects.create(user=self.user1, full_name='User 1 TESTE')
        self.person2 = Person.objects.create(user=self.user2, full_name='User 2 TESTE')
        self.person3 = Person.objects.create(user=self.user3, full_name='User 3 TESTE')

        self.question = Question.objects.create(
            title='O que é sistema monolítico', 
            content='Quais são as principais vantagens de usar uma arquitetura monolítica?', 
            author=self.person1
        )
        
        self.answer = Answer.objects.create(
            question=self.question, 
            content='Um sistema monolítico é uma aplicação onde todas as funcionalidades estão integradas em um único código base.', 
            author=self.person2
            )

    def test_vote_creation(self):
        vote = Vote.objects.create(author=self.person1, answer=self.answer, vote_type=Vote.UPVOTE)
        
        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(vote.author, self.person1)
        self.assertEqual(vote.answer, self.answer)
        self.assertEqual(vote.vote_type, Vote.UPVOTE)

    def test_unique_vote_per_author_answer(self):
        """
        Verifica se um usuário não pode votar mais de uma vez na mesma resposta.
        """
        Vote.objects.create(author=self.person1, answer=self.answer, vote_type=Vote.UPVOTE)
        with self.assertRaises(Exception):
            Vote.objects.create(author=self.person1, answer=self.answer, vote_type=Vote.DOWNVOTE)

    def test_total_votes_property(self):
        """
        Verifica se a propriedade 'total_votes' do Answer calcula a pontuação corretamente.
        """
        self.assertEqual(self.answer.total_votes, 0)

        # 1 Upvote
        Vote.objects.create(author=self.person1, answer=self.answer, vote_type=Vote.UPVOTE)
        self.assertEqual(self.answer.total_votes, 1)

        # 1 Downvote (total deve ser 0)
        Vote.objects.create(author=self.person3, answer=self.answer, vote_type=Vote.DOWNVOTE)
        self.assertEqual(self.answer.total_votes, 0)

        # Mais 1 Upvote (total deve ser 1)
        Vote.objects.create(author=self.person2, answer=self.answer, vote_type=Vote.UPVOTE)
        self.assertEqual(self.answer.total_votes, 1) 

    def test_total_votes_property_after_update(self):
        """
        Verifica se a pontuação é atualizada corretamente após um voto ser modificado.
        """
        vote1 = Vote.objects.create(author=self.person1, answer=self.answer, vote_type=Vote.UPVOTE)
        self.assertEqual(self.answer.total_votes, 1)

        # Modifica o voto para DOWNVOTE
        vote1.vote_type = Vote.DOWNVOTE
        vote1.save()
        self.assertEqual(self.answer.total_votes, -1)

        # Modifica o voto de volta para UPVOTE
        vote1.vote_type = Vote.UPVOTE
        vote1.save()
        self.assertEqual(self.answer.total_votes, 1)
from django.test import TestCase
from django.contrib.auth import get_user_model
from questions.models import Question, Answer
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
        
    def test_answer_creation(self):
        answer = Answer.objects.create(question=self.question, author=self.person1, content="Um sistema monolítico é uma aplicação onde todas as funcionalidades estão integradas em um único código base.")
        
        self.assertEqual(Answer.objects.count(), 1)
        self.assertEqual(answer.author, self.person1)
        self.assertEqual(answer.question, self.question)
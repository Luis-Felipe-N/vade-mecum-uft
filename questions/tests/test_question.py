# questions/tests/test_questions.py
# (You can create this new file or add these tests to an existing test file like test_votes.py)

from django.test import TestCase
from django.contrib.auth import get_user_model
from questions.models import Question, Answer 
from cadastro.models import Person

User = get_user_model() # Ensures we're using your custom user model (e.g., Person)

class QuestionModelTest(TestCase):
    """
    Teste Question model
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            email='q_user@example.com',
            password='password123'
        )
        
        self.person = Person.objects.create(user=self.user, full_name='User 1 TESTE')

    def test_question_creation(self):
        """
        Verifica Questão pode ser criado e salva corretamente.
        """
        question = Question.objects.create(
            title='O que é sistema monolítico', 
            content='Quais são as principais vantagens de usar uma arquitetura monolítica?', 
            author=self.person
        )

        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(question.title, 'O que é sistema monolítico')
        self.assertEqual(question.content, 'Quais são as principais vantagens de usar uma arquitetura monolítica?')
        self.assertEqual(question.author, self.person)

        self.assertIsNotNone(question.created_at)
        self.assertIsNotNone(question.updated_at)
        self.assertTrue(question.created_at <= question.updated_at)

    def test_question_deletion_cascades_answers(self):
        """
        Verifica se remover questions deleta as respostas associadas.
        """
        question = Question.objects.create(
            title='Question to be deleted',
            content='Content here.',
            author=self.person
        )
        Answer.objects.create(question=question, author=self.person, content='Answer 1')
        Answer.objects.create(question=question, author=self.person, content='Answer 2')

        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Answer.objects.count(), 2)

        question.delete()

        self.assertEqual(Question.objects.count(), 0)
        self.assertEqual(Answer.objects.count(), 0)
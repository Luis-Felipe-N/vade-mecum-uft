from django.contrib.auth import get_user_model
from questions.models import Subject, Question, Answer
from cadastro.models import Person
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('pt_BR')

User = get_user_model()

print("--- Gerando Usuários e Perfis de Pessoa ---")
num_users = 10
users = []
for i in range(num_users):
    try:
        username = fake.user_name()
        email = fake.email()
        password = 'password123'

        # Cria o usuário
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.save()
            print(f"Usuário '{username}' criado.")
        else:
            print(f"Usuário '{username}' já existe, pulando.")

        # Cria o perfil de Pessoa associado
        if not hasattr(user, 'person_profile'):
            full_name = fake.name()
            birth_date = fake.date_between(start_date='-40y', end_date='-18y')
            gender = random.choice(['M', 'F', 'O', 'N'])
            enrollment_number = f"UFT{random.randint(10000, 99999)}"
            bio = fake.paragraph(nb_sentences=3)
            
            person = Person.objects.create(
                user=user,
                full_name=full_name,
                birth_date=birth_date,
                gender=gender,
                enrollment_number=enrollment_number,
                bio=bio
            )
            print(f"  Perfil de Pessoa para '{full_name}' criado.")
        else:
            print(f"  Perfil de Pessoa para '{user.person_profile.full_name}' já existe, pulando.")
        users.append(person)
    except Exception as e:
        print(f"Erro ao criar usuário ou perfil: {e}")

if not users:
    print("Nenhum usuário criado. Certifique-se de que o banco de dados está vazio ou ajuste a lógica.")
    users = list(User.objects.all()) 
    if not users:
        print("Ainda sem usuários, crie um superusuário manualmente ou tente novamente.")
        exit()

print("\n--- Gerando Disciplinas (Subjects) ---")
subject_names = [
    "Programação Orientada a Objetos", "Cálculo I", "Álgebra Linear",
    "Estrutura de Dados", "Banco de Dados", "Sistemas Operacionais",
    "Redes de Computadores", "Engenharia de Software", "Inteligência Artificial",
    "Algoritmos e Lógica de Programação", "Física Geral I", "Química Orgânica"
]
subjects = []
for name in subject_names:
    code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3)) + str(random.randint(1000, 9999))
    subject, created = Subject.objects.get_or_create(name=name, defaults={'code': code})
    if created:
        print(f"Disciplina '{name}' criada.")
    else:
        print(f"Disciplina '{name}' já existe, pulando.")
    subjects.append(subject)

if not subjects:
    print("Nenhuma disciplina criada. Verifique Subject model ou adicione manualmente.")
    subjects = list(Subject.objects.all())
    if not subjects:
        print("Ainda sem disciplinas, crie algumas manualmente ou tente novamente.")
        exit()

print("\n--- Gerando Perguntas (Questions) ---")
num_questions = 30
questions = []
for _ in range(num_questions):
    author = random.choice(users)
    subject = random.choice(subjects) if subjects else None
    title = fake.sentence(nb_words=random.randint(5, 10)).replace('.', '?')
    content = fake.paragraph(nb_sentences=random.randint(3, 7))

    file_attachment = None
    if random.random() < 0.3: 
        file_attachment = f"dummy_files/{fake.file_name(category='document', extension='pdf')}"

    question = Question.objects.create(
        title=title,
        content=content,
        author=author,
        subject=subject,
        file_attachment=file_attachment,
        created_at=fake.date_time_between(start_date='-60d', end_date='now', tzinfo=None) 
    )
    questions.append(question)

print("\n--- Gerando Respostas (Answers) ---")
for question in questions:
    num_answers_for_question = random.randint(0, 5)
    answers_for_this_question = []
    for _ in range(num_answers_for_question):
        author = random.choice(users)
        if len(users) > 1 and author == question.author:
            other_users = [u for u in users if u != question.author]
            if other_users:
                author = random.choice(other_users)
            else:
                continue 

        content = fake.paragraph(nb_sentences=random.randint(2, 5))
        
        file_attachment = None
        if random.random() < 0.1:
            file_attachment = f"dummy_files/{fake.file_name(category='document', extension='jpg')}"

        answer = Answer.objects.create(
            question=question,
            content=content,
            author=author,
            file_attachment=file_attachment,
            created_at=fake.date_time_between(start_date=question.created_at, end_date='now', tzinfo=None)
        )
        answers_for_this_question.append(answer)
        

    if answers_for_this_question and random.random() < 0.5: 
        best_answer = random.choice(answers_for_this_question)
        best_answer.is_best_answer = True
        best_answer.save() 
        print(f"  Definida melhor resposta para '{question.title[:30]}...'.")
    else:
        if answers_for_this_question:
            question.update_status() 

print("\n--- Geração de dados fake concluída! ---")
print(f"Total de Usuários: {User.objects.count()}")
print(f"Total de Disciplinas: {Subject.objects.count()}")
print(f"Total de Perguntas: {Question.objects.count()}")
print(f"Total de Respostas: {Answer.objects.count()}")
# questions/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'),
    ]

class Person(models.Model):


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person_profile',
        verbose_name="Usuário Associado",
        help_text="O usuário do sistema associado a este perfil de pessoa."
    )
    full_name = models.CharField(
        max_length=200,
        verbose_name="Nome Completo",
        help_text="Nome completo da pessoa."
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de Nascimento",
        help_text="Data de nascimento da pessoa."
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        verbose_name="Gênero"
    )
    enrollment_number = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Número de Matrícula (UFT)",
        help_text="Número de matrícula do estudante na UFT."
    )

    enrolled_subjects = models.ManyToManyField(
        'Subject', 
        blank=True,
        related_name='students_enrolled',
        verbose_name="Disciplinas Cursadas"
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name="Biografia",
        help_text="Uma breve descrição sobre a pessoa."
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True,
        verbose_name="Foto de Perfil"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name or f"Pessoa ({self.user.username})"

    @property
    def age(self):
        if self.birth_date:
            today = timezone.now().date()
            return today.year - self.birth_date.year - \
                   ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return None

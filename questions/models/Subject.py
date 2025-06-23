from django.db import models

class Subject(models.Model):
    """
    Representa uma disciplina acadêmica (ex: Programação Orientada a Objetos).
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Disciplina")
    code = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="Código da Disciplina")

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
        ordering = ['name']

    def __str__(self):
        return self.name
from django.db import models

#################################
from questions.models import Question
from cadastro.models import Person

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Pergunta"
    )
    content = models.TextField(verbose_name="Conteúdo da Resposta")
    author = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='answers_provided',
        verbose_name="Autor"
    )
    file_attachment = models.FileField(
        upload_to='answer_attachments/',
        null=True,
        blank=True,
        verbose_name="Anexo (Opcional)",
        help_text="Anexe gabaritos, resoluções detalhadas, etc."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    is_best_answer = models.BooleanField(default=False, verbose_name="Melhor Resposta")

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
        ordering = ['created_at'] 

    def __str__(self):
        return f"Resposta de {self.author.username} para '{self.question.title[:30]}...'"

    # Propriedade para garantir que apenas uma resposta pode ser a melhor
    def save(self, *args, **kwargs):
        if self.is_best_answer:
            Answer.objects.filter(question=self.question).exclude(pk=self.pk).update(is_best_answer=False)
            
            self.question.status = 'closed'
            self.question.save(update_fields=['status'])
        elif not self.pk: 
            self.question.update_status() 
        super().save(*args, **kwargs)

    # Adicionando um hook para quando uma resposta é deletada
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.question.update_status()
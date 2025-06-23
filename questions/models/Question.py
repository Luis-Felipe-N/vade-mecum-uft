from django.db import models

STATUS_CHOICES = [
        ('open', 'Aberta'),
        ('answered', 'Respondida'), # Quando tem pelo menos uma resposta
        ('closed', 'Fechada'),     # Quando o autor marcou uma melhor resposta ou encerrou
    ]
class Question(models.Model):

    title = models.CharField(max_length=255, verbose_name="Título da Pergunta")
    content = models.TextField(verbose_name="Conteúdo da Pergunta", help_text="Detalhe sua dúvida ou o que você procura.")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions_asked',
        verbose_name="Autor"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='questions',
        verbose_name="Disciplina"
    )
    file_attachment = models.FileField(
        upload_to='question_attachments/',
        null=True,
        blank=True,
        verbose_name="Anexo (Opcional)",
        help_text="Anexe provas anteriores, enunciados, imagens, etc."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='open',
        verbose_name="Status"
    )
    is_public = models.BooleanField(default=True, verbose_name="Pública") 

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
        ordering = ['-created_at']

    def __str__(self):
        return f"Pergunta: {self.title} por {self.author.username}"

    def update_status(self):
        if self.answers.exists():
            if self.best_answer.exists(): # Se tiver uma melhor resposta, assume-se que está fechada
                self.status = 'closed'
            else:
                self.status = 'answered'
        else:
            self.status = 'open'
        self.save(update_fields=['status'])

    def get_filename(self):
        if self.file_attachment:
            return os.path.basename(self.file_attachment.name)
        return None
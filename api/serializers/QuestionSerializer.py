from rest_framework import serializers
from questions.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'titulo', 'conteudo', 'autor', 'data_criacao']